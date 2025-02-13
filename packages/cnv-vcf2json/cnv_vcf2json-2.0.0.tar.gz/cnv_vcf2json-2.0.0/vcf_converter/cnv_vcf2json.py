#!/usr/bin/env python3
import sys
import json
import argparse
from datetime import datetime

def extract_info(vcf_file, assembly, analysis_id, individual_id, sequence, reference_seq, fusion_id):
    data = []
    biosample_id = None

    with open(vcf_file, 'r') as f:
        for line in f:
            # Capture biosampleId from the header line (#CHROM) (assumes sample is the last column)
            if line.startswith('#CHROM'):
                fields = line.strip().split('\t')
                biosample_id = fields[-1]
            elif line.startswith('#'):
                continue
            else:
                columns = line.strip().split('\t')
                chrom = columns[0]
                pos = int(columns[1])
                legacy_id = columns[2]
                
                # Parse INFO field (key=value pairs; flags become True)
                info = {}
                for item in columns[7].split(';'):
                    if '=' in item:
                        key, value = item.split('=', 1)
                        info[key] = value
                    else:
                        info[item] = True

                # Normalize variant type using ALT field
                variantType = columns[4]
                if "<DEL>" in variantType:
                    variantType = variantType.replace("<DEL>", "DEL")
                elif "<DUP>" in variantType:
                    variantType = variantType.replace("<DUP>", "DUP")

                # Parse FORMAT and sample fields
                format_keys = columns[8].split(':')
                sample_values = columns[9].split(':')
                sample_data = dict(zip(format_keys, sample_values))
                GT = sample_data.get("GT", "")

                # Determine copy number (cn_number)
                cn_number = None
                if "CN" in sample_data:
                    try:
                        cn_number = int(sample_data["CN"])
                    except ValueError:
                        cn_number = None
                else:
                    if variantType == "DEL":
                        if GT in ("0/1", "1/0"):
                            cn_number = 1
                        elif GT == "1/1":
                            cn_number = 0
                    elif variantType == "DUP":
                        cn_number = 3

                # Determine variantState based on cn_number:
                if cn_number is not None:
                    if cn_number == 0:
                        variant_id = "EFO:0030069"
                        variantStateLabel = "complete genomic loss"
                    elif cn_number == 1:
                        variant_id = "EFO:0030068"
                        variantStateLabel = "low-level loss"
                    elif cn_number == 3:
                        variant_id = "EFO:0030071"
                        variantStateLabel = "low-level gain"
                    elif cn_number >= 4:
                        variant_id = "EFO:0030072"
                        variantStateLabel = "high-level gain"
                    else:
                        if variantType == "DEL":
                            variant_id = "EFO:0030067"
                            variantStateLabel = "copy number loss"
                        elif variantType == "DUP":
                            variant_id = "EFO:0030070"
                            variantStateLabel = "copy number gain"
                        else:
                            variant_id = "EFO:0000000"
                            variantStateLabel = "unknown"
                else:
                    if variantType == "DEL":
                        variant_id = "EFO:0030067"
                        variantStateLabel = "copy number loss"
                    elif variantType == "DUP":
                        variant_id = "EFO:0030070"
                        variantStateLabel = "copy number gain"
                    else:
                        variant_id = "EFO:0000000"
                        variantStateLabel = "unknown"

                # Determine the end position (default to pos if not provided)
                end_pos = int(info.get('END', pos))
                # Construct a unique internal variant ID
                variant_internal_id = f"{chrom}:{pos}-{end_pos}:{variant_id}"

                # Build the location object (schema requires 'chromosome', 'start', and 'end')
                location = {
                    "chromosome": chrom.replace("chr", ""),
                    "start": pos,
                    "end": end_pos
                }

                # Build the record according to the Progenetix schema.
                record = {
                    "biosampleId": biosample_id,
                    "variantInternalId": variant_internal_id,
                    "variantState": {
                        "id": variant_id,
                        "label": variantStateLabel
                    },
                    "location": location,
                    "info": {
                        "legacyId": legacy_id,
                        "cn_number": cn_number
                    },
                    "updated": datetime.now().isoformat(),
                    "adjoinedSequences": []
                }
                # Optionally add additional keys if provided
                if assembly:
                    record["assemblyId"] = assembly
                if analysis_id:
                    record["analysisId"] = analysis_id
                if individual_id:
                    record["individualId"] = individual_id
                if sequence:
                    record["sequence"] = sequence
                if reference_seq:
                    record["referenceSequence"] = reference_seq
                if fusion_id:
                    record["fusionId"] = fusion_id

                data.append(record)
    return data

def cnv_vcf2json(args=None):
    parser = argparse.ArgumentParser(
        description="Convert CNVkit VCF to Beacon JSON format following the Progenetix pgxVariant schema"
    )
    # Make input a required positional argument.
    parser.add_argument("input", type=str, help="Input VCF file name")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output JSON file name")
    parser.add_argument("--assembly", type=str, default="", help="Assembly identifier (e.g. GRCh38); if omitted, assemblyId will be excluded")
    parser.add_argument("--analysis", type=str, default="", help="Analysis identifier (analysisId)")
    parser.add_argument("--individual", type=str, default="", help="Individual identifier (individualId)")
    parser.add_argument("--sequence", type=str, default="", help="Variant sequence")
    parser.add_argument("--reference", type=str, default="", help="Reference sequence")
    parser.add_argument("--fusion", type=str, default="", help="Fusion identifier (fusionId)")
    args = parser.parse_args(args)

    input_vcf = args.input
    output_json = args.output
    assembly = args.assembly.strip() if args.assembly.strip() else None
    analysis_id = args.analysis.strip() if args.analysis.strip() else None
    individual_id = args.individual.strip() if args.individual.strip() else None
    sequence = args.sequence.strip() if args.sequence.strip() else None
    reference_seq = args.reference.strip() if args.reference.strip() else None
    fusion_id = args.fusion.strip() if args.fusion.strip() else None

    data = extract_info(input_vcf, assembly, analysis_id, individual_id, sequence, reference_seq, fusion_id)

    with open(output_json, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    cnv_vcf2json(sys.argv[1:])
