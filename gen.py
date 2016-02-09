import subprocess

# TODO fix up the readme so people know what it takes to build this
# TODO fix up the latex document class to have more controlled margins and style
# TODO add formuals to the formula.tex
# TODO add algorithms to src (shortest path, etc)
# TODO compile and tests for src?
# TODO clean up python:
    # Move documents to a text file?
    # Add build / clean / rebuild options?
    # shell=True for everything?
    # column 80 limit?
    # output directly ./output instead of moving afterwards for htmltopdf

cpp_prefix = "./external/reference/en/cpp/";
cpp_documents = [
        "../cpp.html",
        "keyword.html",
        "utility/pair.html",
        "utility/pair/make_pair.html",
        "utility/tuple.html",
        "utility/bitset.html",
        "utility/bitset/set.html",
        "utility/bitset/flip.html",
        "string/basic_string.html",
        "string/basic_string/insert.html",
        "string/basic_string/erase.html",
        "string/basic_string/push_back.html",
        "string/basic_string/compare.html",
        "string/basic_string/replace.html",
        "string/basic_string/substr.html",
        "string/basic_string/find.html",
        "string/basic_string/rfind.html",
        "string/basic_string/find_first_of.html",
        "container/vector.html",
        "container/vector/erase.html",
        "container/vector/push_back.html",
        "container/set.html",
        "container/set/count.html",
        "container/map.html",
        "container/map/map.html",
        "container/map/operator_at.html",
        "container/stack.html",
        "container/priority_queue.html",
        "container/priority_queue/pop.html",
        "algorithm.html",
        "algorithm/search.html",
        "algorithm/fill.html",
        "algorithm/sort.html",
        "algorithm/stable_sort.html",
        "algorithm/lower_bound.html",
        "algorithm/max_element.html",
        "algorithm/next_permutation.html",
        "iterator.html",
        "numeric/math.html",
        "io/basic_iostream.html",
        "language/ascii.html"
    ]

java_prefix = "./external/docs/api/java/"
java_documents = [
        "lang/package-summary.html",
        "lang/Comparable.html",
        "lang/StringBuilder.html",
        "util/package-summary.html",
        "util/Scanner.html",
        "util/Vector.html",
        "util/Hashtable.html",
        "util/HashSet.html",
        "util/PriorityQueue.html",
        "math/BigInteger.html",
        "math/BigDecimal.html",
        "awt/geom/package-summary.html",
        "awt/geom/Point2D.Double.html",
        "awt/geom/Line2D.Double.html",
        "awt/geom/Rectangle2D.Double.html",
        "awt/geom/Arc2D.Double.html",
        "awt/geom/Area.html",
        "util/regex/Pattern.html",
        "util/regex/Matcher.html",
        "util/regex/MatchResult.html"
    ]

destination = "./output/"

cpp_source_pdf = ""
i = 0;
htmltopdf_cmd = "wkhtmltopdf -L 25 --zoom 0.75 -n --enable-local-file-access {0} {1}"
for document in cpp_documents:
    path = cpp_prefix + document
    subprocess.call(htmltopdf_cmd.format(path, "cpp" + str(i) + ".pdf"), shell=True)
    path = "./cpp" + str(i) +".pdf"
    subprocess.call(["mv", path, destination])
    cpp_source_pdf = cpp_source_pdf + destination + "cpp" + str(i) + ".pdf "
    i = i + 1

java_source_pdf = ""
i = 0;
for document in java_documents:
    path = java_prefix + document
    subprocess.call(["wkhtmltopdf", "-L", "25", "--zoom", "0.75", "--enable-local-file-access", path, "java" + str(i) + ".pdf"])
    path = "./java" + str(i) +".pdf"
    subprocess.call(["mv", path, destination])
    java_source_pdf = java_source_pdf + destination + "java" + str(i) + ".pdf "
    i = i + 1

subprocess.call(["rm", "./obj/*"])
subprocess.call(["pdflatex", "-output-directory", "./obj/", "./tex/formulas.tex"])
formulas_pdf = "./obj/formulas.pdf "

src_cmd = "find ./src/*.cpp | xargs enscript --margins 72::: --color -Ecpp -fCourier8 -o - | ps2pdf - code.pdf"
subprocess.call(src_cmd, shell=True)
subprocess.call(["mv", "./code.pdf", destination])
src_pdf = "./output/code.pdf "

args = cpp_source_pdf + formulas_pdf + src_pdf + destination + "main.pdf"
subprocess.call(["pdfunite"] + args.split())
args = java_source_pdf + destination + "javasource.pdf"
subprocess.call(["pdfunite"] + args.split())
