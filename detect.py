#!/usr/bin/env python

import getopt
import chardet
import sys

def usage():
    print "usage"

def main(argv):

    input_file = sys.stdin
    input_file_name = None
    output_file = sys.stdout
    output_file_name = None
    from_codec = None
    to_codec = None
    auto_detect = False
    detect_only = False

    try:
        opts, args = getopt.getopt(argv, "i:o:f:t:ad", ["input=", "output=", "from=", "to=", "auto-decect", "detect-only"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-a", "--auto-decect"):
            auto_detect = True
        elif opt in ("-i", "--input"):
            input_file_name = arg
            input_file = open(arg)
        elif opt in ("-o", "--output"):
            output_file_name = arg
            output_file = open(arg, 'w')
        elif opt in ("-f", "--from"):
            from_codec = arg
        elif opt in ("-t", "--to"):
            to_codec = arg
        elif opt in ("-d", "--detect-only"):
            detect_only = True

    content = get_text(input_file)

    decect_result = chardet.detect(content)

    if detect_only:
        if input_file_name:
            decect_result['file'] = input_file_name
        print decect_result
        return

    if not auto_detect and from_codec is None:
        print "specify codec"
        return

    if auto_detect:
        from_codec = decect_result['encoding']

    if to_codec is None:
        to_codec = from_codec

    result = content.decode(from_codec).encode(to_codec)
    output_file.write(result)

    output_file.close()
    input_file.close()

def get_text(input_file):
    content = ""
    for line in input_file:
        content += line
    return content

if __name__ == '__main__':
    main(sys.argv[1:])