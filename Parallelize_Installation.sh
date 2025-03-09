# Installing dependencies in parallel (Linux/macOS example)
DEPENDENCIES=(
  "llvm"
  "python3"
  "git"
  "make"
  "build-essential"
)

# Run in parallel
echo "${DEPENDENCIES[@]}" | xargs -n 1 -P 4 sudo apt-get install -y
