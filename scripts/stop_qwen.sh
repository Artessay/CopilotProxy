#!/usr/bin/env bash
# Stop any running vLLM server and free the GPU memory it holds.
#
# Why this is needed: `vllm serve` spawns a separate "VLLM::EngineCore" process
# (plus one GPU worker per device for tensor-parallel runs) that actually owns
# the GPU memory. A single Ctrl+C does not always reap those children, and
# `--mm-processor-cache-type shm` leaves a large /dev/shm/VLLM_* buffer behind.
set -u

# 1) Ask the API server to shut down gracefully first.
if pkill -INT -f 'vllm serve'; then
    echo "Sent SIGINT to 'vllm serve', waiting for the GPU to be released..."
    for _ in $(seq 1 15); do
        pgrep -f 'VLLM::' >/dev/null || break
        sleep 1
    done
fi

# 2) Force-kill anything left (engine core / TP workers / api server).
pkill -9 -f 'VLLM::'     2>/dev/null
pkill -9 -f 'vllm serve' 2>/dev/null

# 3) Remove leaked shared-memory buffers.
rm -f /dev/shm/VLLM_* 2>/dev/null

echo "Done. GPU memory per device:"
nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader
