#!/usr/bin/env bash
set -u

base_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
snapshot_dir="${base_dir}/snapshots/2026-09-24"
ledger="${base_dir}/acquisition_ledger_2026-09-24.tsv"
mkdir -p "${snapshot_dir}"

if [[ ! -e "${ledger}" ]]; then
  printf 'source_id\turl\tretrieved_at_utc\thttp_status\tcontent_type\tfile_path\tfile_size_bytes\tsha256\tredistribution_note\n' > "${ledger}"
fi

tail -n +2 "${base_dir}/sources.tsv" |
while IFS=$'\t' read -r source_id url source_type redistribution_note; do
  if [[ -n "${SOURCE_IDS:-}" && ",${SOURCE_IDS}," != *",${source_id},"* ]]; then
    continue
  fi
  extension="html"
  case "${source_type}" in
    *_pdf|standards_pdf) extension="pdf" ;;
  esac
  output="${snapshot_dir}/${source_id}.${extension}"
  if [[ -e "${output}" ]]; then
    output="${snapshot_dir}/${source_id}__$(date -u +'%Y%m%dT%H%M%SZ').${extension}"
  fi
  headers="${snapshot_dir}/${source_id}.headers.txt"
  if [[ -e "${headers}" ]]; then
    headers="${snapshot_dir}/${source_id}__$(date -u +'%Y%m%dT%H%M%SZ').headers.txt"
  fi
  retrieved_at="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  http_status="$(curl --location --silent --show-error \
    --user-agent 'Mozilla/5.0 (compatible; academic-source-archiver/1.0)' \
    --dump-header "${headers}" \
    --output "${output}" \
    --write-out '%{http_code}' \
    "${url}")"
  curl_exit="$?"
  if [[ "${curl_exit}" -ne 0 && -z "${http_status}" ]]; then
    http_status="000"
  fi
  content_type="$(awk 'BEGIN{IGNORECASE=1} /^content-type:/{value=$0} END{sub(/\r$/, "", value); sub(/^[^:]*:[[:space:]]*/, "", value); print value}' "${headers}")"
  if [[ -f "${output}" ]]; then
    file_size="$(stat -c '%s' "${output}")"
    sha256="$(sha256sum "${output}" | cut -d' ' -f1)"
  else
    file_size="0"
    sha256=""
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "${source_id}" "${url}" "${retrieved_at}" "${http_status}" "${content_type}" \
    "${output}" "${file_size}" "${sha256}" "${redistribution_note}" >> "${ledger}"
done
