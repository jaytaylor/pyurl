pyurl
=====

Pyurl allows you to run your own URL shortening service, just like TinyURL, bit.ly, is.gd, etc..

Features:
=========
    - Web-based Configuration
    - Public or private, depending on how you configure it.
    - Links can be randomly generated, sequentially generated, or a custom keyword can be requested.
    - Compatible with any database supported by Django. Uses SQLite by default.
    - XML-RPC & JSON API with associated Documentation.
    - Abuse detection and blocking.
    - Once the shortened url is created, it is automatically copied to the browsers clipboard, allowing users to easily share it anywhere, such as:
        * Twitter
        * Facebook
        * Google+
        * Blogger
        * Delicio.us
        * Digg
        * MySpace?
        * Anywhere!

Requirements:
=============
    - Any WSGI compatible web-server.
    - The configuration that I have tested is to run it as a WSGI module using Apache 2 pre-fork.

Motivation for creating this software
=====================================
Similar Packages: The only standalone url-shortener I could find was PHP-based- YOURLS, but it didn't really suit my needs. The developers also weren't very friendly about the way they packaged their software.

There are already a wide variety of other public url shortening services which will perform the same fundamental function as this software package. However, running your own url-shortening service protects you from problems such as expired urls or websites that may stop providing the service.

