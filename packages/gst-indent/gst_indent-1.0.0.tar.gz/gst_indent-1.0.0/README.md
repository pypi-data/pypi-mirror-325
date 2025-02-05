gst-indent-1.0
==============

gst-indent is a fork of GNU indent 2.2.12, stripped down to the basics and
using Meson as its build system in order to be easily buildable as part of
the GStreamer monorepo on Windows, macOS and Linux and to provide convenient
source code formatting verification on these systems.

By default it also applies the indent options GStreamer uses for its formatting.

The reason we use a custom fork is that GNU indent frequently changes the
formatted output in a way that is not backwards-compatible on new releases,
and often without an option to toggle it back to the previous way of formatting
things. That then forces us to re-indent the entire code base accordingly or
tell developers to stick to an older version, which isn't really a viable
strategy with people using a wide range of distros and distro versions
for their development environment.

By using our custom fork we can stay in control when to apply which updates to
the formatter tool and the formatting, and also provide out-of-the-box local
indentation verification to Windows users working in an MSVC environment.
