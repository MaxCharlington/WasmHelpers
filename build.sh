cat $1 > _tmp.cpp

# Generating bindings
cat _tmp.cpp | sed 's/#include .*$//g' > _tmpNoIncludes.cpp  # TODO: join these steps
python3 ./generateBindings.py _tmpNoIncludes.cpp >> _tmp.cpp

# Append required includes
sed -i "1i/* Generated */\n#include <emscripten/bind.h>\nusing namespace emscripten;\n/* Generated */\n" _tmp.cpp

# Compile
em++ --bind _tmp.cpp -o _ret.js -s USE_SDL=0 -O2

# em++ --bind --no-entry ./test.cpp -o test.wasm -s ENVIRONMENT=web -O0

rm _tmpNoIncludes.cpp
