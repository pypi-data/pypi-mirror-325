indent_sources = [
  'indent.c',
  'args.c',
  'backup.c',
  'comments.c',
  'lexi.c',
  'parse.c',
  'globs.c',
  'code_io.c',
  'output.c',
  'utils.c',
  'handletoken.c',
]

if host_machine.system() == 'windows'
  indent_sources += ['wildexp.c']
endif

# Use the pre-generated sources from the imported tarball if gperf is not available
# (Note: currently we just disable the gperf option by default so this is not used)
gperf = find_program('gperf', required: get_option('gperf'))

# Double-check gperf length type to guard against ancient gperf versions
gperf_len_type = ''
if gperf.found()
  gperf_snippet = run_command(gperf.full_path(), '-L', 'ANSI-C', files('meson-test.gperf')).stdout()
  foreach t : ['size_t', 'unsigned int']
    if cc.compiles('''
                   #include <string.h>
                   const char * in_word_set(const char *, @0@);
                   '''.format(t) + gperf_snippet)
      gperf_len_type = t
      break
    endif
  endforeach
endif

if gperf.found() and gperf_len_type == 'size_t'
  gperf_c_inc = configure_file(output: 'gperf.c.inc',
    input: 'indent.gperf',
    command: [gperf, '-D', '-c', '-l', '-p', '-t', '-T', '-g', '-j1', '-o', '-K',
                     'rwd', '-L', 'ANSI-C', '-N', 'is_reserved',
                     '@INPUT@', '--output-file', '@OUTPUT@'])

  gperf_cc_c_inc = configure_file(output: 'gperf-cc.c.inc',
    input: 'indent-cc.gperf',
    command: [gperf, '-D', '-c', '-l', '-p', '-t', '-T', '-g', '-j1', '-o', '-K',
                     'rwd', '-L', 'ANSI-C', '-N', 'is_reserved_cc', '-H', 'hash_cc',
                     '@INPUT@', '--output-file', '@OUTPUT@'])
else
  gperf_c_inc = configure_file(output: 'gperf.c.inc',
    input: 'gperf.c',
    copy: true)

  gperf_cc_c_inc = configure_file(output: 'gperf-cc.c.inc',
    input: 'gperf-cc.c',
    copy: true)
endif

gst_indent_exe = executable(prog_name, indent_sources,
  c_args: ['-DMESON_BUILD', '-DGNU_INDENT_FORK_VERSION="2.2.12"'],
  include_directories: indent_incs,
  install: not meson.is_subproject(),
  dependencies: deps,
  native: true)

# Make gst-indent-1.0 usable for other subprojects
if meson.is_subproject() and meson.can_run_host_binaries()
  meson.override_find_program('gst-indent-1.0', gst_indent_exe)
endif
