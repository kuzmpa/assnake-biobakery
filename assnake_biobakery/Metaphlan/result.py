
import os
from assnake.core.Result import Result

result = Result.from_location(name='Metaphlan',
                              description='Taxa annotation',
                              result_type='taxa',
                              input_type='illumina_sample',
                              with_presets=False,
                              preset_file_format='yaml',
                              location=os.path.dirname(os.path.abspath(__file__)))
