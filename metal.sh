#!/bin/bash

NUM_POSTS=20
CONTENT_DIR=content
LOREM_API=https://jaspervdj.be/lorem-markdownum/markdown.txt
IMAGES_API=https://placeimg.com/1000/341/animals

rm -fR content
mkdir -p content/images

for i in $(seq -w 1 ${NUM_POSTS})
do
    post_file=${CONTENT_DIR}/post${i}.markdown

    echo "Creating post ${i}"
    echo "Title: A sample article ${i}" >> ${post_file}
    echo "Date: 2021-03-${i}" >> ${post_file}
    echo "Category: News" >> ${post_file}
    echo "Tags: $(seq 1 20 | shuf | head -n3 | sed -r s,"^","tag", | paste -sd "," -)" >> ${post_file}
    echo "Image: post${i}.jpg" >> ${post_file}
    echo "Summary: Summary of post ${i}" >> ${post_file}
    echo >> ${post_file}

    curl -s ${LOREM_API} | sed -r s,"^#","##", >> ${post_file}

    curl -s ${IMAGES_API} > ${CONTENT_DIR}/images/post${i}.jpg
done
