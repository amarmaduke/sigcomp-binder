import subprocess

converter = "wkhtmltopdf {0} {1}"

prefix = "./external/reference/en/cpp/";
documents = [
        "../cpp.html",
        "keyword.html",
        "operator_precedence.html",
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

cpp_source_pdf = ""

i = 0;
for document in documents:
    path = prefix + document;
    subprocess.call(["wkhtmltopdf", "-L", "25", "--allow", "./external/reference/common", "--enable-local-file-access", path, str(i) + ".pdf"])
    path = "./" + str(i) +".pdf"
    destination = "./output/"
    subprocess.call(["mv", path, destination])
    cpp_source_pdf = cpp_source_pdf + destination + str(i) + ".pdf "
    i = i + 1

args = cpp_source_pdf + destination + "source.pdf"
subprocess.call(["pdfunite"] + args.split())

