
PIG_SCRIPT="script.pig"

pig $PIG_SCRIPT

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

OUTPUT_DIR="/path/to/output"

if [ -d "$OUTPUT_DIR" ]; then
  mv "$OUTPUT_DIR" "${OUTPUT_DIR}-${TIMESTAMP}"
fi

mkdir -p "$OUTPUT_DIR"

echo "Pig script executed and output stored in ${OUTPUT_DIR}-${TIMESTAMP}"
