
#!/bin/sh
if [ $# -eq 0 ]; then
echo "ClojureScript command line tool"
echo ""
echo "Usage:"
echo " cljs new myproj (creates new ClojureScript project)"
echo " cljs gui (starts the ClojureScript compiler GUI)"
exit 1
fi
if [ $1 = "new" ]; then
echo "Creating new ClojureScript project at $2..."
shift # consume first argument "new"
lein new mies "$@"
echo "Done."
else
lein cljsbuild "$@"
fi
