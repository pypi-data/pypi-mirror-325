# Minimal Meson build for GNU indent
project('indent', 'c', version: '1.0.0',
  license: 'GPL-3.0-or-later',
  meson_version: '>= 0.56',
  default_options: [
    'c_std=gnu99',
    # skips the declspec madness of bundled libintl
    'default_library=static'
  ]
)

cc = meson.get_compiler('c', native: true)

thread_dep = dependency('threads')

warn_cargs = cc.get_supported_arguments([
  '-Wno-unused-value',
  '-Wredundant-decls',
  '-Wshadow',
  '-Wstrict-prototypes',
  '-Wmissing-prototypes',
  '-Wnested-externs',
  '-Wmissing-declarations',
  '-Wcomment',
  '-Wbad-function-cast',
  '-Wcast-align',
])

add_project_arguments('-DHAVE_CONFIG_H', warn_cargs, language: 'c', native: true)

# c11 enables usage of bundled libintl on MSVC (_STDC_VERSION_ macro)
# unfortunately we need to support vs2017
if cc.get_define('_MSC_VER ') != '' and cc.version().version_compare('< 19.28')
  add_project_arguments(cc.get_supported_arguments([
    '-D__STDC_VERSION__=199901L',
  ]), language: 'c', native: true)
endif

deps = [thread_dep]

corefoundation_dep = dependency('appleframeworks', modules : 'foundation', required: false)

if corefoundation_dep.found()
  deps += [corefoundation_dep]
endif

indent_incs = include_directories('.')

cdata = configuration_data()

prog_name = get_option('executable-name')
cdata.set_quoted('PROG_NAME', prog_name)

# Extra default options for GStreamer, in addition to normal indent defaults
extra_opts_arr = [
  '--braces-on-if-line',
  '--case-brace-indentation0',
  '--case-indentation2',
  '--braces-after-struct-decl-line',
  '--line-length80',
  '--no-tabs',
  '--cuddle-else',
  '--dont-line-up-parentheses',
  '--continuation-indentation4',
  '--honour-newlines',
  '--tab-size8',
  '--indent-level2',
  '--leave-preprocessor-space',
]
cdata.set('EXTRA_DEFAULT_OPTIONS', '"' + '","'.join(extra_opts_arr) + '"')

cdata.set('IGNORE_PROFILE', get_option('ignore-profile'))

cdata.set_quoted('PACKAGE', 'indent')

cdata.set('STDC_HEADERS', true)

if cc.compiles('''#define __EXTENSIONS__ 1
int
main (void)
{

  ;
  return 0;
}''', name: 'whether it is safe to define __EXTENSIONS__')
  cdata.set10('__EXTENSIONS__', true)
  cdata.set10('_ALL_SOURCE', true)
  cdata.set10('_GNU_SOURCE', true)
  cdata.set10('_POSIX_PTHREAD_SEMANTICS', true)
  cdata.set10('_TANDEM_SOURCE', true)
endif

check_funcs = [
  'asprintf',
  'fwprintf',
  'newlocale',
  'putenv',
  'setenv',
  'setlocale',
  'snprintf',
  'strnlen',
  'wcslen',
  'wcsnlen',
  'mbrtowc',
  'wcrtomb',
  'memcpy',
  'memmove',
  'setlocale',
  'strchr',
  'utime',
  'getcwd',
  'getegid',
  'geteuid',
  'getgid',
  'getuid',
  'mempcpy',
  'munmap',
  'stpcpy',
  'strcasecmp',
  'strdup',
  'strtoul',
  'tsearch',
  'uselocale',
  'argz_count',
  'argz_stringify',
  'argz_next',
  '__fsetlocking',
  'symlink',
  'wprintf', # MANUAL
]
foreach f : check_funcs
  macro = 'HAVE_@0@'.format(f.underscorify().to_upper())
  cdata.set10(macro, cc.compiles('''/* Define @0@ to an innocuous variant, in case <limits.h> declares @0@.
   For example, HP-UX 11i <limits.h> declares gettimeofday.  */
#define @0@ innocuous_@0@

/* System header to define __stub macros and hopefully few prototypes,
   which can conflict with char @0@ (); below.  */

#include <limits.h>
#undef @0@

/* Override any GCC internal prototype to avoid an error.
   Use char because int might match the return type of a GCC
   builtin and then its argument prototype would still apply.  */
#ifdef __cplusplus
extern "C"
#endif
char @0@ ();
/* The GNU C library defines this for functions which it implements
    to always fail with ENOSYS.  Some functions are actually named
    something starting with __ and the normal name is an alias.  */
#if defined __stub_@0@ || defined __stub___@0@
choke me
#endif

int
main (void)
{
return @0@ ();
  ;
  return 0;
}'''.format(f), name: 'has @0@ (builtins are not accepted)'.format(f)))
endforeach

check_headers = [
  'alloca.h',
  'sys/types.h',
  'sys/stat.h',
  'stdlib.h',
  'string.h',
  'memory.h',
  'strings.h',
  'inttypes.h',
  'stdint.h',
  'unistd.h',
  'locale.h',
  'malloc.h',
  'utime.h',
  'sys/utime.h',
  'argz.h',
  'limits.h',
  'sys/param.h',
]
foreach h : check_headers
  macro = 'HAVE_@0@'.format(h.underscorify().to_upper())
  if cc.has_header(h) # they rely on both #if defined and #if
    cdata.set10(macro, true)
  endif
endforeach

dirent_h = [
  'dirent.h',
  'sys/ndir.h',
  'sys/dir.h',
  'ndir.h',
]
foreach h : dirent_h
  macro = 'HAVE_@0@'.format(h.underscorify().to_upper())
  if cc.has_type('DIR', prefix: '#include <@0@>'.format(h))
    cdata.set10(macro, true)
    break
  else
    cdata.set(macro, false)
  endif
endforeach

if cc.has_header_symbol('malloc.h', 'alloca') or cc.has_header_symbol('alloca.h', 'alloca')
  cdata.set10('HAVE_ALLOCA', true)
endif

cdata.set10('HAVE_LANGINFO_CODESET', cc.links('''#include <langinfo.h>
int main()
{
  char* cs = nl_langinfo(CODESET); return !cs;
}
''', name: 'you have <langinfo.h> and nl_langinfo(CODESET)'))

fcntl_h = '''#include <sys/types.h>
#include <sys/stat.h>
#if @0@
# include <unistd.h>
#else /* on Windows with MSVC */
# include <io.h>
# include <stdlib.h>
# defined sleep(n) _sleep ((n) * 1000)
#endif
#include <fcntl.h>
#ifndef O_NOATIME
#define O_NOATIME 0
#endif
#ifndef O_NOFOLLOW
#define O_NOFOLLOW 0
#endif
static int const constants[] =
{
  O_CREAT, O_EXCL, O_NOCTTY, O_TRUNC, O_APPEND,
  O_NONBLOCK, O_SYNC, O_ACCMODE, O_RDONLY, O_RDWR, O_WRONLY
};
int main()
{
[[
int result = !constants;
#if @1@
{
  static char const sym[] = "conftest.sym";
  if (symlink ("/dev/null", sym) != 0)
    result |= 2;
  else
    {
      int fd = open (sym, O_WRONLY | O_NOFOLLOW | O_CREAT, 0);
      if (fd >= 0)
        {
          close (fd);
          result |= 4;
        }
    }
  if (unlink (sym) != 0 || symlink (".", sym) != 0)
    result |= 2;
  else
    {
      int fd = open (sym, O_RDONLY | O_NOFOLLOW);
      if (fd >= 0)
        {
          close (fd);
          result |= 4;
        }
    }
  unlink (sym);
}
#endif
{
  static char const file[] = "confdefs.h";
  int fd = open (file, O_RDONLY | O_NOATIME);
  if (fd < 0)
    result |= 8;
  else
    {
      struct stat st0;
      if (fstat (fd, &st0) != 0)
        result |= 16;
      else
        {
          char c;
          sleep (1);
          if (read (fd, &c, 1) != 1)
            result |= 24;
          else
            {
              if (close (fd) != 0)
                result |= 32;
              else
                {
                  struct stat st1;
                  if (stat (file, &st1) != 0)
                    result |= 40;
                  else
                    if (st0.st_atime != st1.st_atime)
                      result |= 64;
                }
            }
        }
    }
}
return result;
}'''.format(cdata.get('HAVE_UNISTD_H', 0), cdata.get('HAVE_SYMLINK', 0))

if meson.is_cross_build()
  cdata.set('HAVE_WORKING_O_NOATIME', false)
  cdata.set('HAVE_WORKING_O_NOFOLLOW', false)
else
  working_fcntl_h = cc.run(fcntl_h, args: ['-D_GNU_SOURCE'])

  if working_fcntl_h.returncode() == 0
    cdata.set10('HAVE_WORKING_O_NOATIME', true)
    cdata.set10('HAVE_WORKING_O_NOFOLLOW', true)
  else
    if working_fcntl_h.returncode() != 4 and working_fcntl_h.returncode() != 68
      cdata.set10('HAVE_WORKING_O_NOATIME', true)
    else
      cdata.set('HAVE_WORKING_O_NOATIME', false)
    endif
    if working_fcntl_h.returncode() != 64 and working_fcntl_h.returncode() != 68
      cdata.set10('HAVE_WORKING_O_NOFOLLOW', true)
    else
      cdata.set('HAVE_WORKING_O_NOFOLLOW', false)
    endif
  endif
endif

int_divbyzero_sigfpe = target_machine.system() == 'darwin' and target_machine.cpu_family().contains('x86')

if not int_divbyzero_sigfpe
  if meson.is_cross_build()
    int_divbyzero_sigfpe = ['x86', 'x86_64', 's390', 's390x', 'alpha', 'm68k'].contains(target_machine.cpu_family())
  else
    int_divbyzero_sigfpe = cc.run('''#include <stdlib.h>
#include <signal.h>

static void
sigfpe_handler (int sig)
{
  /* Exit with code 0 if SIGFPE, with code 1 if any other signal.  */
  exit (sig != SIGFPE);
}

int x = 1;
int y = 0;
int z;
int nan;

int main ()
{
  signal (SIGFPE, sigfpe_handler);
/* IRIX and AIX (when "xlc -qcheck" is used) yield signal SIGTRAP.  */
#if (defined (__sgi) || defined (_AIX)) && defined (SIGTRAP)
  signal (SIGTRAP, sigfpe_handler);
#endif
/* Linux/SPARC yields signal SIGILL.  */
#if defined (__sparc__) && defined (__linux__)
  signal (SIGILL, sigfpe_handler);
#endif

  z = x / y;
  nan = y / y;
  exit (2);
}''', name: 'whether integer division by zero raises SIGFPE').returncode() == 0
  endif
endif

cdata.set10('INTDIV0_RAISES_SIGFPE', int_divbyzero_sigfpe)

if meson.is_cross_build()
  cdata.set10('HAVE_POSIX_PRINTF',
    (cc.get_define('_MSC_VER') != '')
    or (cc.get_define('__MINGW32__') != '')
    or (target_machine.system() == 'netbsd')
    or (target_machine.system() == 'cygwin'))
else
  cdata.set10('HAVE_POSIX_PRINTF', cc.run('''#include <stdio.h>
#include <string.h>
/* The string "%2$d %1$d", with dollar characters protected from the shell's
   dollar expansion (possibly an autoconf bug).  */
static char format[] = { '%', '2', '$', 'd', ' ', '%', '1', '$', 'd', '\0' };
static char buf[100];
int main ()
{
  sprintf (buf, format, 33, 55);
  return (strcmp (buf, "55 33") != 0);
}''',
  name: 'whether printf() supports POSIX/XSI format strings').returncode() == 0)
endif

cdata.set10('HAVE_INTMAX_T', cc.has_type('intmax_t', prefix: '#include <stdint.h>') or cc.has_type('intmax_t', prefix: '#include <inttypes.h>'))

cdata.set10('HAVE_INTTYPES_H_WITH_UINTMAX', cc.compiles('''#include <sys/types.h>
#include <inttypes.h>
int main()
{
  uintmax_t i = (uintmax_t) -1; return !i;
}''', name: '<inttypes.h> exists, doesn\'t clash with <sys/types.h>, and declares uintmax_t' ))

if not cc.compiles('''#include <inttypes.h>
#ifdef PRId32
char *p = PRId32;
#endif''', name: 'whether the inttypes.h PRIxNN macros are broken]')
  cdata.set10('PRI_MACROS_BROKEN', true)
else
  cdata.set('PRI_MACROS_BROKEN', false)
endif

if cc.has_header_symbol('locale.h', 'LC_MESSAGES')
  cdata.set10('HAVE_LC_MESSAGES', true)
else
  cdata.set('HAVE_LC_MESSAGES', false)
endif

cdata.set10('HAVE_PTHREAD_RWLOCK', cc.has_type('pthread_rwlock_t', prefix: '#include <pthread.h>', dependencies: thread_dep, args: ['-D_GNU_SOURCE']))
cdata.set10('HAVE_PTHREAD_MUTEX_RECURSIVE', cc.compiles('''
#include <pthread.h>
int main()
{
#if __FreeBSD__ == 4
error "No, in FreeBSD 4.0 recursive mutexes actually don't work."
#elif (defined __ENVIRONMENT_MAC_OS_X_VERSION_MIN_REQUIRED__ \
       && __ENVIRONMENT_MAC_OS_X_VERSION_MIN_REQUIRED__ < 1070)
error "No, in Mac OS X < 10.7 recursive mutexes actually don't work."
#else
int x = (int)PTHREAD_MUTEX_RECURSIVE;
return !x;
#endif
}
''', name: 'if <pthread.h> defines PTHREAD_MUTEX_RECURSIVE'))

cdata.set10('HAVE_LONG_LONG_INT', cc.has_type('long long int'))
cdata.set10('HAVE_UNSIGNED_LONG_LONG_INT', cc.has_type('unsigned long long int'))

cdata.set10('HAVE_STDINT_H_WITH_UINTMAX', cc.compiles('''
#include <sys/types.h>
#include <stdint.h>
int main()
{
  uintmax_t i = (uintmax_t) -1; return !i;
}
''',
  name: '<stdint.h> exists, doesn\'t clash with <sys/types.h>, and declares uintmax_t'))

if cc.links('''extern void xyzzy ();
#pragma weak xyzzy
int main()
{
  xyzzy();
  return 0;
}''', name: 'whether imported symbols can be declared weak')
  if meson.is_cross_build()
    have_weak = cc.get_define('__ELF__') == '1'
  else
    have_weak = cc.run('''
      #include <stdio.h>
      #pragma weak fputs
      int main ()
      {
        return (fputs == NULL);
      }
    ''').returncode() == 0
  endif
else
  have_weak = false
endif

have_pthread = cc.has_header('pthread.h', dependencies: thread_dep)

if have_pthread
  have_pthread = cc.has_function('pthread_mutex_lock', prefix: '#include <pthread.h>', dependencies: thread_dep) and cc.has_function('pthread_mutexattr_init', prefix: '#include <pthread.h>', dependencies: thread_dep)
  cdata.set('PTHREAD_IN_USE_DETECTION_HARD', target_machine.system() == 'sunos')
  if have_pthread
    cdata.set10('USE_POSIX_THREADS', true)
    cdata.set10('USE_POSIX_THREADS_WEAK', have_weak)
  endif
elif target_machine.system() == 'sunos'
  cdata.set10('USE_SOLARIS_THREADS', true)
  cdata.set10('USE_SOLARIS_THREADS_WEAK', have_weak)
elif target_machine.system() == 'windows'
  cdata.set10('USE_WINDOWS_THREADS', true)
endif

if cc.has_type('uintmax_t', prefix: '''#include <stdint.h>
#include <inttypes.h>''')
  cdata.set10('HAVE_UINTMAX_T', true)
else
  cdata.set('uintmax_t', 'size_t')
endif

cdata.set10('HAVE_VISIBILITY', cc.has_function_attribute('visibility:hidden'))

cdata.set10('HAVE_WCHAR_T', cc.has_type('wchar_t', prefix: '#include <stddef.h>'))

cdata.set10('HAVE_WINT_T', cc.has_type('wint_t', prefix: '''#include <stddef.h>
#include <stdio.h>
#include <time.h>
#include <wchar.h>'''))

if cdata.get('HAVE_UTIME', 0) == 1 and cdata.get('HAVE_SYS_UTIME_H', 0) == 1
  if cc.has_type('struct utimbuf',
    prefix: '''#include <sys/types.h>
    #include <utime.h>''')
    utimbuf_needs_posix = false
  else
    utimbuf_needs_posix = cc.has_type('struct utimbuf',
      prefix: '''#include <sys/types.h>
      #include <utime.h>''',
      args: ['-posix']
    )
  endif

  if utimbuf_needs_posix
    add_project_arguments(['-posix'], language: ['c'])
  endif
endif

prefix = get_option('prefix')

cdata.set_quoted('LOCALEDIR', prefix / get_option('localedir'))
cdata.set_quoted('VERSION', meson.project_version())

subdir('src')

configure_file(output: 'config.h', configuration: cdata)
