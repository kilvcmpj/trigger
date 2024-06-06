#!/bin/bash

NEXT_TOKEN=""
WORKFLOWS=()

while : ; do
    if [ -z "$NEXT_TOKEN" ]; then
        RESPONSE=$(aws glue list-workflows)
    else
        RESPONSE=$(aws glue list-workflows --next-token "$NEXT_TOKEN")
    fi

    # Extract workflows from the response and append them to the WORKFLOWS array
    NEW_WORKFLOWS=$(echo $RESPONSE | jq -r '.Workflows[]')
    WORKFLOWS+=($NEW_WORKFLOWS)

    # Extract NextToken
    NEXT_TOKEN=$(echo $RESPONSE | jq -r '.NextToken')

    # If there's no NextToken, break the loop
    if [ "$NEXT_TOKEN" == "null" ]; then
        break
    fi
done

# Output all workflows
for workflow in "${WORKFLOWS[@]}"; do
    echo $workflow
done
