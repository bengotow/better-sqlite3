{
  'variables': {
      'sqlite_version%':'3140100',
      "toolset%":'',
  },
  'target_defaults': {
    'default_configuration': 'Release',
    'msbuild_toolset':'<(toolset)',
    'configurations': {
      'Debug': {
        'defines!': [
          'NDEBUG'
        ],
        'cflags_cc!': [
          '-O3',
          '-Os',
          '-DNDEBUG'
        ],
        'xcode_settings': {
          'MACOSX_DEPLOYMENT_TARGET': '10.7',
          'OTHER_CPLUSPLUSFLAGS!': [
            '-O3',
            '-Os',
            '-DDEBUG'
          ],
          'OTHER_CFLAGS': [
            '-DHAVE_USLEEP=1'
          ],
          'GCC_OPTIMIZATION_LEVEL': '0',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES'
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1, # /EHsc
          }
        }
      },
      'Release': {
        'defines': [
          'NDEBUG'
        ],
        'xcode_settings': {
          'MACOSX_DEPLOYMENT_TARGET': '10.7',
          'OTHER_CPLUSPLUSFLAGS!': [
            '-Os',
            '-O2'
          ],
          'OTHER_CFLAGS': [
            '-DHAVE_USLEEP=1'
          ],
          'GCC_OPTIMIZATION_LEVEL': '3',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
          'DEAD_CODE_STRIPPING': 'YES',
          'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES'
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1, # /EHsc
          }
        }
      }
    }
  }
}
