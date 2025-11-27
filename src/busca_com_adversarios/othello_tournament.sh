#!/usr/bin/env bash

base_path="advsearch/acm_agent"

count_agent="${base_path}/othello_minimax_count.py"
mask_agent="${base_path}/othello_minimax_mask.py"
custom_agent="${base_path}/othello_minimax_custom.py"

echo "Starting Othello tournament between agents..."

echo "Count Agent vs Mask Agent"
conda run --name ufrgs-ia python server.py othello ${count_agent} ${mask_agent} --log-history count_vs_mask.log --output-file count_vs_mask.out
echo

echo "Count Agent vs Custom Agent"
conda run --name ufrgs-ia python server.py othello ${count_agent} ${custom_agent} --log-history count_vs_custom.log --output-file count_vs_custom.out
echo

echo "Mask Agent vs Count Agent"
conda run --name ufrgs-ia python server.py othello ${mask_agent} ${count_agent} --log-history mask_vs_count.log --output-file mask_vs_count.out
echo

echo "Mask Agent vs Custom Agent"
conda run --name ufrgs-ia python server.py othello ${mask_agent} ${custom_agent} --log-history mask_vs_custom.log --output-file mask_vs_custom.out
echo

echo "Custom Agent vs Count Agent"
conda run --name ufrgs-ia python server.py othello ${custom_agent} ${count_agent} --log-history custom_vs_count.log --output-file custom_vs_count.out
echo

echo "Custom Agent vs Mask Agent"
conda run --name ufrgs-ia python server.py othello ${custom_agent} ${mask_agent} --log-history custom_vs_mask.log --output-file custom_vs_mask.out
echo

echo "Tournament finished."
