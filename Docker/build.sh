#!/usr/bin/env bash

TAG=""
LOCAL_NAME="moc_prices_source"
IS_BETA=0
AWS_ID=""
AWS_REGION="us-west-1"

usage() {
    echo "Usage: $0 [-i|--id AWS_ID] [-r|--region AWS_REGION]"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -i|--id)
            AWS_ID="$2"
            shift 2
            ;;
        -r|--region)
            AWS_REGION="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
    esac
done

NAMESPACES=(ghcr.io/money-on-chain/$LOCAL_NAME)

if [ -n "$AWS_ID" ] && [ -n "$AWS_REGION" ]; then
    NAMESPACES+=("$AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$LOCAL_NAME")
fi

# Exit immediately if a command exits with a non-zero status
set -e 

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Go one level up from the script's directory
TARGET_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$TARGET_DIR"

# Get version
VERSION=$(cat moc_prices_source/version.txt)

# Assign VERSION to TAG only if TAG is empty or unset
: "${TAG:=$VERSION}"

# Default NAME if NAME is empty or unset
: "${LOCAL_NAME:=moc_prices_source}"

# Verify is beta
if [ "$IS_BETA" -eq 1 ]; then
    if ! echo "$TAG" | grep -iq "b"; then
        TAG="${TAG}-beta"
    fi
else
    if echo "$TAG" | grep -iq "b"; then
        IS_BETA=1
    fi
fi

# Build
docker build --pull --no-cache -t "$LOCAL_NAME" -f Docker/Dockerfile .

# Tags
docker tag "$LOCAL_NAME" "$LOCAL_NAME:$TAG"
docker tag "$LOCAL_NAME" "$LOCAL_NAME:latest"

PUSH_TAGS=()
for NAMESPACE in "${NAMESPACES[@]}"; do
    docker tag "$LOCAL_NAME:$TAG" "$NAMESPACE:$TAG"
    PUSH_TAGS+=("$NAMESPACE:$TAG")
    if [ "$IS_BETA" -ne 1 ]; then
        docker tag "$LOCAL_NAME:$TAG" "$NAMESPACE:latest"
        PUSH_TAGS+=("$NAMESPACE:latest")
    else
        docker tag "$LOCAL_NAME:$TAG" "$NAMESPACE:beta"
        PUSH_TAGS+=("$NAMESPACE:beta")
    fi
done

# Show local images
IMG_ID=$( docker images --format '{{.ID}}' "$LOCAL_NAME" | sort | uniq )
IMG_SIZE=$( docker images --format '{{.Size}}' "$LOCAL_NAME" | sort | uniq )
echo ""
echo "Local images ($IMG_ID: $IMG_SIZE):"
docker images --format '---> {{.Repository}}:{{.Tag}}|{{.ID}}' | grep "$IMG_ID" | cut -d '|' -f1

echo ""
echo "Local registry tags created:"
printf '  %s\n' "${PUSH_TAGS[@]}"

# Push
echo ""
echo "To upload the image you must run:"
for NAMESPACE in "${NAMESPACES[@]}"; do
    echo ""
    if [ -n "$AWS_ID" ] && [ "$NAMESPACE" = "$AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$LOCAL_NAME" ]; then
        echo "~$ aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
    fi
    echo "~$ docker push $NAMESPACE:$TAG"
    if [ "$IS_BETA" -ne 1 ]; then
        echo "~$ docker push $NAMESPACE:latest"
    else
        echo "~$ docker push $NAMESPACE:beta"
    fi
done

# END.
echo ""
