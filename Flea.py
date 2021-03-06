#   An IRC bot named Flea
#   Copyright (C) 2016  Kris Lamoureux

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>

import traceback
import sys

try:
    import core.main

except KeyboardInterrupt:
    print "\nGoodbye!"
    sys.exit()

except SystemExit:
    raise

except:
    # Print error, save it to error.txt
    # then wait to be closed.
    traceback.print_exc()

    errorfile = open("error.txt", 'a')
    traceback.print_exc(None, errorfile)
    errorfile.close()

    raw_input()
    sys.exit(0)

