steps:

- name: 'gcr.io/cloud-builders/docker'
  args: ['build',
         '-t', 'gcr.io//:',
         '-t', 'gcr.io//:latest', '.'
        ]

- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io//:']

substitutions:
  _IMAGE_NAME: ml/asciitree

images: [
  'gcr.io//:latest',
  'gcr.io//:'
]
