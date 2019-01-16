"""File Searcher"""
import collections
import os

from tp_common import print_header

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header('File Searcher')
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry we cant search for nothing!")
        return

    matches = search_folders(folder, text)

    if not matches:
        print('No match found')
    else:
        count = 0
        for m in matches:
            count += 1
            print('-------Match-------')
            print("file: {}\nline: {}\nmatch: {}".format(
                m.file, m.line, m.text.strip()))

        print('Found {} matches'.format(count))


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(text=line, file=filename, line=line_num)
                yield m  # matches.append(m)

        # return matches


def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # matches = search_folders(full_item, text)
            yield from search_folders(full_item, text)  # more succinct generator
        else:
            # matches = search_file(full_item, text)
            yield from search_file(full_item, text)

        # all_matches.extend(matches)
        # for m in matches:
        #     yield m
    # return all_matches


if __name__ == '__main__':
    main()
