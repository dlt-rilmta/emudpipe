#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

from xtsv import build_pipeline, parser_skeleton, jnius_config


def main():

    argparser = parser_skeleton(description='emUDPipe - An UDPipe wrapper for e-magyar (xtsv).')
    opts = argparser.parse_args()

    jnius_config.classpath_show_warning = opts.verbose  # Suppress warning.

    # Set input and output iterators...
    if opts.input_text is not None:
        input_data = opts.input_text
    else:
        input_data = opts.input_stream
    output_iterator = opts.output_stream

    # Set the tagger name as in the tools dictionary
    used_tools = ['udpipe-tok-parse']
    presets = []

    # Init and run the module as it were in xtsv

    # The relevant part of config.py
    emudpipe_tok_parse = ('emudpipe.emudpipe', 'UDPipe',
                          'UDPipe tokenizer, POS tagger and dependency parser as a whole',
                          (), {'task': 'tok-parse', 'source_fields': set(),
                               'target_fields': ['form', 'lemma', 'upostag', 'feats', 'head', 'deprel', 'deps']})

    tools = [(emudpipe_tok_parse, ('udpipe-tok-parse',))]

    # Run the pipeline on input and write result to the output...
    output_iterator.writelines(build_pipeline(input_data, used_tools, tools, presets, opts.conllu_comments))

    # TODO this method is recommended when debugging the tool
    # Alternative: Run specific tool for input (still in emtsv format):
    # from xtsv import process
    # from emdummy import EmDummy
    # output_iterator.writelines(process(input_data, EmDummy(*em_dummy[3], **em_dummy[4])))

    # Alternative2: Run REST API debug server
    # from xtsv import pipeline_rest_api, singleton_store_factory
    # app = pipeline_rest_api('TEST', tools, {},  conll_comments=False, singleton_store=singleton_store_factory(),
    #                         form_title='TEST TITLE', doc_link='https://github.com/dlt-rilmta/emdummy')
    # app.run()


if __name__ == '__main__':
    main()
