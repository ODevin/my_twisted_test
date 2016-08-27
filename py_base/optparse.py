import optparse, os, socket, time


def parse_args():
    usage = 'hahhahahahhahahahahhahahahhahahh'

    parser = optparse.OptionParser(usage)

    help = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')

    help = "The number of seconds between sending bytes."
    parser.add_option('--delay', type='float', help=help, default=.7)

    help = "The number of bytes to send at a time."
    parser.add_option('--num-bytes', type='int', help=help, default=10)

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('Provide exactly one poetry file.')

    poetry_file = args[0]

    print(poetry_file)
    print(options)
    # return options, poetry_file

parse_args()