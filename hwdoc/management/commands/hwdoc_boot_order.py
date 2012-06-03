# -*- coding: utf-8 -*- vim:encoding=utf-8:
# vim: tabstop=4:shiftwidth=4:softtabstop=4:expandtab

# Copyright © 2010-2012 Greek Research and Technology Network (GRNET S.A.)
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.
'''
Django management command to change boot order
'''

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from hwdoc.models import Model, Equipment, ServerManagement
from hwdoc.functions import search

import sys
import csv
import re
from optparse import make_option

class Command(BaseCommand):
    '''
    Django management command to change boot order
    '''
    help = 'Sets boot order. Once off is supported if backend supports it'
    args = '[key]'
    label = search.__doc__

    option_list = BaseCommand.option_list + (
                make_option('-o', '--once',
                    action='store_true',
                    dest='once',
                    default=False,
                    help='Set once off boot device. --list argument is also needed. Only first value used'),
                make_option('-l', '--list',
                    action='store',
                    type='string',
                    dest='boot_list',
                    help='Comma separated list of boot devices. Valid values depend on backend'),
                make_option('-u', '--username',
                    action='store',
                    type='string',
                    dest='username',
                    default=None,
                    help='Provide username used to login to BMC'),
                make_option('-p', '--password',
                    action='store',
                    type='string',
                    dest='password',
                    default=None,
                    help='Provide password used to login to BMC'),
            )

    def handle(self, *args, **options):
        '''
        Handle command
        '''

        if args is None or len(args) != 1:
            raise CommandError("You must supply a key")

        try:
            key = args[0]
        except IndexError:
            print "Error in usage. See help"
            sys.exit(1)

        es = search(key)
        if es.count() == 0:
            print "No Equipment found"
            return

        for e in es:
            try:
                e.servermanagement
            except ServerManagement.DoesNotExist: 
                continue
            if int(options['verbosity']) > 1:
                print e
            ops = {'once': options['once'], 'boot_list': options['boot_list'].split(',')}
            result = e.servermanagement.boot_order(options['username'], options['password'], **ops)
            #TODO: Figure out what to do with this
            if int(options['verbosity']) > 1:
                print result
