# -*- coding: utf-8 -*-

import sys
import argparse
import logging

from docfu import Docfu

def parse_args(argv):
    """ Parse command line arguments. """

    argp = argparse.ArgumentParser()

    argp.add_argument('-b', '--branch', 
        help="A git branch to checkout.")
    argp.add_argument('-t', '--tag', 
        help="A git tag to checkout.")
    argp.add_argument('-r', '--root-dir', default='docs/',
            help="Root directory which docs are built from.")
    argp.add_argument('--source-dir', default="docs/src", 
        help="Source directory which to compile from.")
    argp.add_argument('--templates-dir', default="docs/templates", 
        help="Directory to look for Jinaj2 templates in.")
    argp.add_argument('--assets-dir', default="docs/assets", 
        help="Directory to look for assets (css, js & images) in.")
    argp.add_argument('uri', nargs=1, 
        help="A URI pointing to a file path, git repository, or github shortened repo.")
    argp.add_argument('destination', nargs=1, 
        help="Destination for compiled source.")
    argp.add_argument("-c", "--config", 
            help="A configuration file to read (not implemented)")
    argp.add_argument("-v", "--verbose", action='store_true', default=False,
            help="Run verbosely or not.")

    options = argp.parse_args(argv)

    return vars(options)

def init_logger(verbose):
    logging.basicConfig()
    logger = logging.getLogger('docfu')
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

def main(argv=None):
    """ Main """

    if not argv:
        argv = sys.argv[1:]

    options = parse_args(argv)
    uri = options.get('uri')[0]
    dest = options.get('destination')[0]
    root = options.get('root_dir')
    del options['uri']
    del options['destination']
    del options['root_dir']

    init_logger(options.get('verbose', False))
    with Docfu(uri, root, dest, **options) as df:
        df()

    return 0 # success

if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)

