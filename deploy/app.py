#!/usr/bin/env python3

from aws_cdk import core

from django_vue.frontend import FrontendStack
from django_vue.networking import NetworkingAndDBStack

app = core.App()
FrontendStack(app, "django_vue-frontend")
NetworkingAndDBStack(app, "django_vue-networking-db")

app.synth()
