cat $1 > tmp/_.cpp

filename=$(basename -- "$1")
filename="${filename%.*}"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Generating bindings
cat tmp/_.cpp | sed 's/#include .*$//g' > tmp/NoIncludes.cpp  # TODO: join these steps
python3 scripts/generate_bindings.py tmp/NoIncludes.cpp >> tmp/_.cpp

# Append required includes
sed -i "1i/* Generated */\n#include <emscripten/bind.h>\nusing namespace emscripten;\n/* Generated */\n" tmp/_.cpp

# Compile
em++ --bind tmp/_.cpp -o public/compiled/${filename}.js -s USE_SDL=0 -O2 -s ENVIRONMENT=web
