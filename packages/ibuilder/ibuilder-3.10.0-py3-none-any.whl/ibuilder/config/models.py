#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  SPDX-License-Identifier: GPL-3.0-only
#  Copyright 2024 dradux.com

from typing import List, Optional

from pydantic import BaseModel


class Application(BaseModel):
    """
    Application.
    """

    name: str = None
    version: str = None


class Build(BaseModel):
    """
    Build components such as the image, args, and dockerfile.
    """

    image: bool = True
    args: List = None
    labels: List = None
    base_path: str = "."
    dockerfile: str = "Dockerfile"
    repository: str = None
    tag_image_latest: bool = False
    # note: version is not required as it is calculated if not supplied.
    version: Optional[str] = None
    network_mode: Optional[str] = None


class Config(BaseModel):
    """
    Configuration components such as the database path.
    """

    component: str = None
    dbpath: str = None


class History(BaseModel):
    """ "
    History components such as
    """

    save_request_canceled: bool = False


class PushRegistry(BaseModel):
    """
    Push registry components such as url, username, etc.
    """

    url: str | None
    username: str | None
    password: Optional[str] | None
    # email: Optional[str] | None


class Push(BaseModel):
    """
    Push components such as the image, registry, and docker config path.
    """

    image: bool = True
    registry: PushRegistry = None
    docker_config_path: Optional[str] = "$HOME/.docker/config.json"


class Sign(BaseModel):
    """
    Sign components such as whether to sign and what signer to use.
    """

    enabled: bool = False
    signor: str = ""


class Source(BaseModel):
    """
    Source components such as whether to tag the source image.
    """

    tag: bool = False
    push_tag: bool = False


class Internal(BaseModel):
    """
    Internal (application) config.
    """

    application: Application = None


class Project(BaseModel):
    """
    Project configuration.
    """

    build: Build = Build()
    push: Push = Push()
    sign: Sign = Sign()
    source: Source = Source()
    history: History = History()
    config: Config = Config()
