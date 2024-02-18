# PHP2Python

Python alternatives for PHP internal (built-in) functions. Support Python 3
Only.

- [php2go](https://github.com/syyongx/php2go) - Use Golang to implement
  PHP's common built-in functions

## Table of Contents

- [Array Functions](#array-functions)
- [Date/Time Functions](#datetime-functions)
- [Filesystem Functions](#filesystem-functions)
- [Mathematical Functions](#mathematical-functions)
- [Misc. Functions](#misc-functions)
- [Network Functions](#network-functions)
- [Program execution Functions](#program-execution-functions)
- [String Functions](#string-functions)
- [URL Functions](#url-functions)
- [Variable handling Functions](#variable-handling-functions)

## Array Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [x] [array_change_key_case](https://php.net/manual/en/function.array-change-key-case.php)
  — Changes the case of all keys in an array
- [x] [array_chunk](https://php.net/manual/en/function.array-chunk.php) —
  Split an array into chunks
- [x] [array_column](https://php.net/manual/en/function.array-column.php) —
  Return the values from a single column in the input array
- [x] [array_combine](https://php.net/manual/en/function.array-combine.php)
  — Creates an array by using one array for keys and another for its values
- [x] [array_count_values](https://php.net/manual/en/function.array-count-values.php)
  — Counts all the values of an array
- [ ] [array_diff_assoc](https://php.net/manual/en/function.array-diff-assoc.php)
  — Computes the difference of arrays with additional index check
- [ ] [array_diff_key](https://php.net/manual/en/function.array-diff-key.php)
  — Computes the difference of arrays using keys for comparison
- [ ] [array_diff_uassoc](https://php.net/manual/en/function.array-diff-uassoc.php)
  — Computes the difference of arrays with additional index check which is
  performed by a user supplied callback function
- [ ] [array_diff_ukey](https://php.net/manual/en/function.array-diff-ukey.php)
  — Computes the difference of arrays using a callback function on the keys
  for comparison
- [x] [array_diff](https://php.net/manual/en/function.array-diff.php) —
  Computes the difference of arrays
- [x] [array_fill_keys](https://php.net/manual/en/function.array-fill-keys.php)
  — Fill an array with values, specifying keys
- [x] [array_fill](https://php.net/manual/en/function.array-fill.php) — Fill
  an array with values
- [x] [array_filter](https://php.net/manual/en/function.array-filter.php) —
  Filters elements of an array using a callback function
- [x] [array_flip](https://php.net/manual/en/function.array-flip.php) —
  Exchanges all keys with their associated values in an array
- [ ] [array_intersect_assoc](https://php.net/manual/en/function.array-intersect-assoc.php)
  — Computes the intersection of arrays with additional index check
- [ ] [array_intersect_key](https://php.net/manual/en/function.array-intersect-key.php)
  — Computes the intersection of arrays using keys for comparison
- [ ] [array_intersect_uassoc](https://php.net/manual/en/function.array-intersect-uassoc.php)
  — Computes the intersection of arrays with additional index check,
  compares indexes by a callback function
- [ ] [array_intersect_ukey](https://php.net/manual/en/function.array-intersect-ukey.php)
  — Computes the intersection of arrays using a callback function on the
  keys for comparison
- [ ] [array_intersect](https://php.net/manual/en/function.array-intersect.php)
  — Computes the intersection of arrays
- [x] [array_key_exists](https://php.net/manual/en/function.array-key-exists.php)
  — Checks if the given key or index exists in the array
- [x] [array_key_first](https://php.net/manual/en/function.array-key-first.php)
  — Gets the first key of an array
- [x] [array_key_last](https://php.net/manual/en/function.array-key-last.php)
  — Gets the last key of an array
- [x] [array_keys](https://php.net/manual/en/function.array-keys.php) —
  Return all the keys or a subset of the keys of an array
- [x] [array_map](https://php.net/manual/en/function.array-map.php) —
  Applies the callback to the elements of the given arrays
- [x] [array_merge_recursive](https://php.net/manual/en/function.array-merge-recursive.php)
  — Merge one or more arrays recursively
- [x] [array_merge](https://php.net/manual/en/function.array-merge.php) —
  Merge one or more arrays
- [ ] [array_multisort](https://php.net/manual/en/function.array-multisort.php)
  — Sort multiple or multi-dimensional arrays
- [x] [array_pad](https://php.net/manual/en/function.array-pad.php) — Pad
  array to the specified length with a value
- [x] [array_pop](https://php.net/manual/en/function.array-pop.php) — Pop
  the element off the end of array
- [x] [array_product](https://php.net/manual/en/function.array-product.php)
  — Calculate the product of values in an array
- [x] [array_push](https://php.net/manual/en/function.array-push.php) — Push
  one or more elements onto the end of array
- [ ] [array_rand](https://php.net/manual/en/function.array-rand.php) — Pick
  one or more random keys out of an array
- [x] [array_reduce](https://php.net/manual/en/function.array-reduce.php) —
  Iteratively reduce the array to a single value using a callback function
- [x] [array_replace_recursive](https://php.net/manual/en/function.array-replace-recursive.php)
  — Replaces elements from passed arrays into the first array recursively
- [ ] [array_replace](https://php.net/manual/en/function.array-replace.php)
  — Replaces elements from passed arrays into the first array
- [x] [array_reverse](https://php.net/manual/en/function.array-reverse.php)
  — Return an array with elements in reverse order
- [ ] [array_search](https://php.net/manual/en/function.array-search.php) —
  Searches the array for a given value and returns the first corresponding
  key if successful
- [x] [array_shift](https://php.net/manual/en/function.array-shift.php) —
  Shift an element off the beginning of array
- [x] [array_slice](https://php.net/manual/en/function.array-slice.php) —
  Extract a slice of the array
- [x] [array_splice](https://php.net/manual/en/function.array-splice.php) —
  Remove a portion of the array and replace it with something else
- [x] [array_sum](https://php.net/manual/en/function.array-sum.php) —
  Calculate the sum of values in an array
- [ ] [array_udiff_assoc](https://php.net/manual/en/function.array-udiff-assoc.php)
  — Computes the difference of arrays with additional index check, compares
  data by a callback function
- [ ] [array_udiff_uassoc](https://php.net/manual/en/function.array-udiff-uassoc.php)
  — Computes the difference of arrays with additional index check, compares
  data and indexes by a callback function
- [ ] [array_udiff](https://php.net/manual/en/function.array-udiff.php) —
  Computes the difference of arrays by using a callback function for data
  comparison
- [ ] [array_uintersect_assoc](https://php.net/manual/en/function.array-uintersect-assoc.php)
  — Computes the intersection of arrays with additional index check,
  compares data by a callback function
- [ ] [array_uintersect_uassoc](https://php.net/manual/en/function.array-uintersect-uassoc.php)
  — Computes the intersection of arrays with additional index check,
  compares data and indexes by separate callback functions
- [ ] [array_uintersect](https://php.net/manual/en/function.array-uintersect.php)
  — Computes the intersection of arrays, compares data by a callback
  function
- [x] [array_unique](https://php.net/manual/en/function.array-unique.php) —
  Removes duplicate values from an array
- [x] [array_unshift](https://php.net/manual/en/function.array-unshift.php)
  — Prepend one or more elements to the beginning of an array
- [x] [array_values](https://php.net/manual/en/function.array-values.php) —
  Return all the values of an array
- [ ] [array_walk_recursive](https://php.net/manual/en/function.array-walk-recursive.php)
  — Apply a user function recursively to every member of an array
- [ ] [array_walk](https://php.net/manual/en/function.array-walk.php) —
  Apply a user supplied function to every member of an array
- [ ] [array](https://php.net/manual/en/function.array.php) — Create an
  array
- [ ] [arsort](https://php.net/manual/en/function.arsort.php) — Sort an
  array in reverse order and maintain index association
- [ ] [asort](https://php.net/manual/en/function.asort.php) — Sort an array
  and maintain index association
- [x] [compact](https://php.net/manual/en/function.compact.php) — Create
  array containing variables and their values
- [x] [count](https://php.net/manual/en/function.count.php) — Count all
  elements in an array, or something in an object
- [ ] [current](https://php.net/manual/en/function.current.php) — Return the
  current element in an array
- [ ] [each](https://php.net/manual/en/function.each.php) — Return the
  current key and value pair from an array and advance the array cursor
- [x] [end](https://php.net/manual/en/function.end.php) — Set the internal
  pointer of an array to its last element
- [ ] [extract](https://php.net/manual/en/function.extract.php) — Import
  variables into the current symbol table from an array
- [x] [in_array](https://php.net/manual/en/function.in-array.php) — Checks
  if a value exists in an array
- [x] [key_exists](https://php.net/manual/en/function.key-exists.php) —
  Alias of array_key_exists
- [ ] [key](https://php.net/manual/en/function.key.php) — Fetch a key from
  an array
- [x] [krsort](https://php.net/manual/en/function.krsort.php) — Sort an
  array by key in reverse order
- [x] [ksort](https://php.net/manual/en/function.ksort.php) — Sort an array
  by key
- [ ] <strike>[list](https://php.net/manual/en/function.list.php) — Assign
  variables as if they were an array</strike>,
  `Built-in function in Python`
- [ ] [natcasesort](https://php.net/manual/en/function.natcasesort.php) —
  Sort an array using a case insensitive "natural order" algorithm
- [ ] [natsort](https://php.net/manual/en/function.natsort.php) — Sort an
  array using a "natural order" algorithm
- [ ] <strike>[next](https://php.net/manual/en/function.next.php) — Advance
  the internal pointer of an array</strike>, `Built-in function in Python`
- [ ] [pos](https://php.net/manual/en/function.pos.php) — Alias of current
- [ ] [prev](https://php.net/manual/en/function.prev.php) — Rewind the
  internal array pointer
- [ ] <strike>[range](https://php.net/manual/en/function.range.php) — Create
  an array containing a range of elements</strike>,
  `Built-in function in Python`
- [ ] [reset](https://php.net/manual/en/function.reset.php) — Set the
  internal pointer of an array to its first element
- [x] [rsort](https://php.net/manual/en/function.rsort.php) — Sort an array
  in reverse order
- [x] [shuffle](https://php.net/manual/en/function.shuffle.php) — Shuffle an
  array
- [x] [sizeof](https://php.net/manual/en/function.sizeof.php) — Alias of
  count
- [x] [sort](https://php.net/manual/en/function.sort.php) — Sort an array
- [ ] [uasort](https://php.net/manual/en/function.uasort.php) — Sort an
  array with a user-defined comparison function and maintain index
  association
- [ ] [uksort](https://php.net/manual/en/function.uksort.php) — Sort an
  array by keys using a user-defined comparison function
- [ ] [usort](https://php.net/manual/en/function.usort.php) — Sort an array
  by values using a user-defined comparison function

## Date/Time Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [x] [checkdate](https://php.net/manual/en/function.checkdate.php) —
  Validate a Gregorian date
- [ ] <strike>[date_add](https://php.net/manual/en/function.date-add.php) —
  Alias of DateTime::add</strike>
- [ ] <strike>[date_create_from_format](https://php.net/manual/en/function.date-create-from-format.php)
  — Alias of DateTime::createFromFormat</strike>
- [ ] <strike>[date_create_immutable_from_format](https://php.net/manual/en/function.date-create-immutable-from-format.php)
  — Alias of DateTimeImmutable::createFromFormat</strike>
- [ ] <strike>[date_create_immutable](https://php.net/manual/en/function.date-create-immutable.php)
  — Alias of DateTimeImmutable::\_\_construct</strike>
- [ ] <strike>[date_create](https://php.net/manual/en/function.date-create.php)
  — Alias of DateTime::\_\_construct</strike>
- [ ] <strike>[date_date_set](https://php.net/manual/en/function.date-date-set.php)
  — Alias of DateTime::setDate</strike>
- [x] [date_default_timezone_get](https://php.net/manual/en/function.date-default-timezone-get.php)
  — Gets the default timezone used by all date/time functions in a script
- [ ] [date_default_timezone_set](https://php.net/manual/en/function.date-default-timezone-set.php)
  — Sets the default timezone used by all date/time functions in a script
- [ ] <strike>[date_diff](https://php.net/manual/en/function.date-diff.php)
  — Alias of DateTime::diff</strike>
- [ ] <strike>[date_format](https://php.net/manual/en/function.date-format.php)
  — Alias of DateTime::format</strike>
- [ ] <strike>[date_get_last_errors](https://php.net/manual/en/function.date-get-last-errors.php)
  — Alias of DateTime::getLastErrors</strike>
- [ ] <strike>[date_interval_create_from_date_string](https://php.net/manual/en/function.date-interval-create-from-date-string.php)
  — Alias of DateInterval::createFromDateString</strike>
- [ ] <strike>[date_interval_format](https://php.net/manual/en/function.date-interval-format.php)
  — Alias of DateInterval::format</strike>
- [ ] <strike>[date_isodate_set](https://php.net/manual/en/function.date-isodate-set.php)
  — Alias of DateTime::setISODate</strike>
- [ ] <strike>[date_modify](https://php.net/manual/en/function.date-modify.php)
  — Alias of DateTime::modify</strike>
- [ ] <strike>[date_offset_get](https://php.net/manual/en/function.date-offset-get.php)
  — Alias of DateTime::getOffset</strike>
- [ ] [date_parse_from_format](https://php.net/manual/en/function.date-parse-from-format.php)
  — Get info about given date formatted according to the specified format
- [ ] [date_parse](https://php.net/manual/en/function.date-parse.php) —
  Returns associative array with detailed info about given date
- [ ] <strike>[date_sub](https://php.net/manual/en/function.date-sub.php) —
  Alias of DateTime::sub</strike>
- [ ] [date_sun_info](https://php.net/manual/en/function.date-sun-info.php)
  — Returns an array with information about sunset/sunrise and twilight
  begin/end
- [ ] [date_sunrise](https://php.net/manual/en/function.date-sunrise.php) —
  Returns time of sunrise for a given day and location
- [ ] <strike>[date_sunset](https://php.net/manual/en/function.date-sunset.php)
  — Returns time of sunset for a given day and location</strike>
- [ ] <strike>[date_time_set](https://php.net/manual/en/function.date-time-set.php)
  — Alias of DateTime::setTime</strike>
- [ ] <strike>[date_timestamp_get](https://php.net/manual/en/function.date-timestamp-get.php)
  — Alias of DateTime::getTimestamp</strike>
- [ ] <strike>[date_timestamp_set](https://php.net/manual/en/function.date-timestamp-set.php)
  — Alias of DateTime::setTimestamp</strike>
- [ ] <strike>[date_timezone_get](https://php.net/manual/en/function.date-timezone-get.php)
  — Alias of DateTime::getTimezone</strike>
- [ ] <strike>[date_timezone_set](https://php.net/manual/en/function.date-timezone-set.php)
  — Alias of DateTime::setTimezone</strike>
- [x] [date](https://php.net/manual/en/function.date.php) — Format a local
  time/date
- [ ] [getdate](https://php.net/manual/en/function.getdate.php) — Get
  date/time information
- [ ] [gettimeofday](https://php.net/manual/en/function.gettimeofday.php) —
  Get current time
- [ ] [gmdate](https://php.net/manual/en/function.gmdate.php) — Format a
  GMT/UTC date/time
- [ ] [gmmktime](https://php.net/manual/en/function.gmmktime.php) — Get Unix
  timestamp for a GMT date
- [ ] [gmstrftime](https://php.net/manual/en/function.gmstrftime.php) —
  Format a GMT/UTC time/date according to locale settings
- [ ] [idate](https://php.net/manual/en/function.idate.php) — Format a local
  time/date as integer
- [x] [localtime](https://php.net/manual/en/function.localtime.php) — Get
  the local time
- [x] [microtime](https://php.net/manual/en/function.microtime.php) — Return
  current Unix timestamp with microseconds
- [x] [mktime](https://php.net/manual/en/function.mktime.php) — Get Unix
  timestamp for a date
- [ ] [strftime](https://php.net/manual/en/function.strftime.php) — Format a
  local time/date according to locale settings
- [ ] [strptime](https://php.net/manual/en/function.strptime.php) — Parse a
  time/date generated with strftime
- [ ] [strtotime](https://php.net/manual/en/function.strtotime.php) — Parse
  about any English textual datetime description into a Unix timestamp
- [x] [time](https://php.net/manual/en/function.time.php) — Return current
  Unix timestamp
- [ ] <strike>[timezone_abbreviations_list](https://php.net/manual/en/function.timezone-abbreviations-list.php)
  — Alias of DateTimeZone::listAbbreviations</strike>
- [ ] <strike>[timezone_identifiers_list](https://php.net/manual/en/function.timezone-identifiers-list.php)
  — Alias of DateTimeZone::listIdentifiers</strike>
- [ ] <strike>[timezone_location_get](https://php.net/manual/en/function.timezone-location-get.php)
  — Alias of DateTimeZone::getLocation</strike>
- [ ] [timezone_name_from_abbr](https://php.net/manual/en/function.timezone-name-from-abbr.php)
  — Returns the timezone name from abbreviation
- [ ] <strike>[timezone_name_get](https://php.net/manual/en/function.timezone-name-get.php)
  — Alias of DateTimeZone::getName</strike>
- [ ] <strike>[timezone_offset_get](https://php.net/manual/en/function.timezone-offset-get.php)
  — Alias of DateTimeZone::getOffset</strike>
- [ ] <strike>[timezone_open](https://php.net/manual/en/function.timezone-open.php)
  — Alias of DateTimeZone::\_\_construct</strike>
- [ ] <strike>[timezone_transitions_get](https://php.net/manual/en/function.timezone-transitions-get.php)
  — Alias of DateTimeZone::getTransitions</strike>
- [ ] [timezone_version_get](https://php.net/manual/en/function.timezone-version-get.php)
  — Gets the version of the timezonedb

## Filesystem Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [x] [basename](https://php.net/manual/en/function.basename.php) — Returns
  trailing name component of path
- [x] [chgrp](https://php.net/manual/en/function.chgrp.php) — Changes file
  group
- [x] [chmod](https://php.net/manual/en/function.chmod.php) — Changes file
  mode
- [x] [chown](https://php.net/manual/en/function.chown.php) — Changes file
  owner
- [ ] [clearstatcache](https://php.net/manual/en/function.clearstatcache.php)
  — Clears file status cache
- [x] [copy](https://php.net/manual/en/function.copy.php) — Copies file
- [x] [delete](https://php.net/manual/en/function.delete.php) — See unlink
  or unset
- [x] [dirname](https://php.net/manual/en/function.dirname.php) — Returns a
  parent directory's path
- [ ] [disk_free_space](https://php.net/manual/en/function.disk-free-space.php)
  — Returns available space on filesystem or disk partition
- [ ] [disk_total_space](https://php.net/manual/en/function.disk-total-space.php)
  — Returns the total size of a filesystem or disk partition
- [ ] [diskfreespace](https://php.net/manual/en/function.diskfreespace.php)
  — Alias of disk_free_space
- [ ] [fclose](https://php.net/manual/en/function.fclose.php) — Closes an
  open file pointer
- [ ] [feof](https://php.net/manual/en/function.feof.php) — Tests for
  end-of-file on a file pointer
- [x] [fflush](https://php.net/manual/en/function.fflush.php) — Flushes the
  output to a file
- [ ] [fgetc](https://php.net/manual/en/function.fgetc.php) — Gets character
  from file pointer
- [ ] [fgetcsv](https://php.net/manual/en/function.fgetcsv.php) — Gets line
  from file pointer and parse for CSV fields
- [ ] [fgets](https://php.net/manual/en/function.fgets.php) — Gets line from
  file pointer
- [ ] [fgetss](https://php.net/manual/en/function.fgetss.php) — Gets line
  from file pointer and strip HTML tags
- [x] [file_exists](https://php.net/manual/en/function.file-exists.php) —
  Checks whether a file or directory exists
- [ ] [file_get_contents](https://php.net/manual/en/function.file-get-contents.php)
  — Reads entire file into a string
- [x] [file_put_contents](https://php.net/manual/en/function.file-put-contents.php)
  — Write data to a file
- [ ] [file](https://php.net/manual/en/function.file.php) — Reads entire
  file into an array
- [x] [fileatime](https://php.net/manual/en/function.fileatime.php) — Gets
  last access time of file
- [x] [filectime](https://php.net/manual/en/function.filectime.php) — Gets
  inode change time of file
- [x] [filegroup](https://php.net/manual/en/function.filegroup.php) — Gets
  file group
- [x] [fileinode](https://php.net/manual/en/function.fileinode.php) — Gets
  file inode
- [x] [filemtime](https://php.net/manual/en/function.filemtime.php) — Gets
  file modification time
- [x] [fileowner](https://php.net/manual/en/function.fileowner.php) — Gets
  file owner
- [x] [fileperms](https://php.net/manual/en/function.fileperms.php) — Gets
  file permissions
- [x] [filesize](https://php.net/manual/en/function.filesize.php) — Gets
  file size
- [ ] [filetype](https://php.net/manual/en/function.filetype.php) — Gets
  file type
- [x] [flock](https://php.net/manual/en/function.flock.php) — Portable
  advisory file locking
- [x] [fnmatch](https://php.net/manual/en/function.fnmatch.php) — Match
  filename against a pattern
- [ ] [fopen](https://php.net/manual/en/function.fopen.php) — Opens file or
  URL
- [ ] [fpassthru](https://php.net/manual/en/function.fpassthru.php) — Output
  all remaining data on a file pointer
- [ ] [fputcsv](https://php.net/manual/en/function.fputcsv.php) — Format
  line as CSV and write to file pointer
- [ ] [fputs](https://php.net/manual/en/function.fputs.php) — Alias of
  fwrite
- [x] [fread](https://php.net/manual/en/function.fread.php) — Binary-safe
  file read
- [ ] [fscanf](https://php.net/manual/en/function.fscanf.php) — Parses input
  from a file according to a format
- [x] [fseek](https://php.net/manual/en/function.fseek.php) — Seeks on a
  file pointer
- [x] [fstat](https://php.net/manual/en/function.fstat.php) — Gets
  information about a file using an open file pointer
- [x] [ftell](https://php.net/manual/en/function.ftell.php) — Returns the
  current position of the file read/write pointer
- [x] [ftruncate](https://php.net/manual/en/function.ftruncate.php) —
  Truncates a file to a given length
- [ ] [fwrite](https://php.net/manual/en/function.fwrite.php) — Binary-safe
  file write
- [x] [glob](https://php.net/manual/en/function.glob.php) — Find pathnames
  matching a pattern
- [x] [is_dir](https://php.net/manual/en/function.is-dir.php) — Tells
  whether the filename is a directory
- [x] [is_executable](https://php.net/manual/en/function.is-executable.php)
  — Tells whether the filename is executable
- [x] [is_file](https://php.net/manual/en/function.is-file.php) — Tells
  whether the filename is a regular file
- [x] [is_link](https://php.net/manual/en/function.is-link.php) — Tells
  whether the filename is a symbolic link
- [x] [is_readable](https://php.net/manual/en/function.is-readable.php) —
  Tells whether a file exists and is readable
- [ ] [is_uploaded_file](https://php.net/manual/en/function.is-uploaded-file.php)
  — Tells whether the file was uploaded via HTTP POST
- [x] [is_writable](https://php.net/manual/en/function.is-writable.php) —
  Tells whether the filename is writable
- [x] [is_writeable](https://php.net/manual/en/function.is-writeable.php) —
  Alias of is_writable
- [x] [lchgrp](https://php.net/manual/en/function.lchgrp.php) — Changes
  group ownership of symlink
- [x] [lchown](https://php.net/manual/en/function.lchown.php) — Changes user
  ownership of symlink
- [x] [link](https://php.net/manual/en/function.link.php) — Create a hard
  link
- [x] [linkinfo](https://php.net/manual/en/function.linkinfo.php) — Gets
  information about a link
- [x] [lstat](https://php.net/manual/en/function.lstat.php) — Gives
  information about a file or symbolic link
- [x] [mkdir](https://php.net/manual/en/function.mkdir.php) — Makes
  directory
- [ ] [move_uploaded_file](https://php.net/manual/en/function.move-uploaded-file.php)
  — Moves an uploaded file to a new location
- [ ] [parse_ini_file](https://php.net/manual/en/function.parse-ini-file.php)
  — Parse a configuration file
- [ ] [parse_ini_string](https://php.net/manual/en/function.parse-ini-string.php)
  — Parse a configuration string
- [ ] [pathinfo](https://php.net/manual/en/function.pathinfo.php) — Returns
  information about a file path
- [ ] [pclose](https://php.net/manual/en/function.pclose.php) — Closes
  process file pointer
- [ ] [popen](https://php.net/manual/en/function.popen.php) — Opens process
  file pointer
- [x] [readfile](https://php.net/manual/en/function.readfile.php) — Outputs
  a file
- [x] [readlink](https://php.net/manual/en/function.readlink.php) — Returns
  the target of a symbolic link
- [ ] [realpath_cache_get](https://php.net/manual/en/function.realpath-cache-get.php)
  — Get realpath cache entries
- [ ] [realpath_cache_size](https://php.net/manual/en/function.realpath-cache-size.php)
  — Get realpath cache size
- [x] [realpath](https://php.net/manual/en/function.realpath.php) — Returns
  canonicalized absolute pathname
- [x] [rename](https://php.net/manual/en/function.rename.php) — Renames a
  file or directory
- [ ] [rewind](https://php.net/manual/en/function.rewind.php) — Rewind the
  position of a file pointer
- [x] [rmdir](https://php.net/manual/en/function.rmdir.php) — Removes
  directory
- [ ] [set_file_buffer](https://php.net/manual/en/function.set-file-buffer.php)
  — Alias of stream_set_write_buffer
- [x] [stat](https://php.net/manual/en/function.stat.php) — Gives
  information about a file
- [x] [symlink](https://php.net/manual/en/function.symlink.php) — Creates a
  symbolic link
- [ ] [tempnam](https://php.net/manual/en/function.tempnam.php) — Create
  file with unique file name
- [ ] [tmpfile](https://php.net/manual/en/function.tmpfile.php) — Creates a
  temporary file
- [x] [touch](https://php.net/manual/en/function.touch.php) — Sets access
  and modification time of file
- [x] [umask](https://php.net/manual/en/function.umask.php) — Changes the
  current umask
- [x] [unlink](https://php.net/manual/en/function.unlink.php) — Deletes a
  file

## Mathematical Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [ ] <strike>[abs](https://php.net/manual/en/function.abs.php) — Absolute
  value</strike>, `Built-in function in Python`
- [x] [acos](https://php.net/manual/en/function.acos.php) — Arc cosine
- [x] [acosh](https://php.net/manual/en/function.acosh.php) — Inverse
  hyperbolic cosine
- [x] [asin](https://php.net/manual/en/function.asin.php) — Arc sine
- [x] [asinh](https://php.net/manual/en/function.asinh.php) — Inverse
  hyperbolic sine
- [x] [atan2](https://php.net/manual/en/function.atan2.php) — Arc tangent of
  two variables
- [x] [atan](https://php.net/manual/en/function.atan.php) — Arc tangent
- [x] [atanh](https://php.net/manual/en/function.atanh.php) — Inverse
  hyperbolic tangent
- [x] [base_convert](https://php.net/manual/en/function.base-convert.php) —
  Convert a number between arbitrary bases
- [x] [bindec](https://php.net/manual/en/function.bindec.php) — Binary to
  decimal
- [x] [ceil](https://php.net/manual/en/function.ceil.php) — Round fractions
  up
- [x] [cos](https://php.net/manual/en/function.cos.php) — Cosine
- [x] [cosh](https://php.net/manual/en/function.cosh.php) — Hyperbolic
  cosine
- [x] [decbin](https://php.net/manual/en/function.decbin.php) — Decimal to
  binary
- [x] [dechex](https://php.net/manual/en/function.dechex.php) — Decimal to
  hexadecimal
- [x] [decoct](https://php.net/manual/en/function.decoct.php) — Decimal to
  octal
- [x] [deg2rad](https://php.net/manual/en/function.deg2rad.php) — Converts
  the number in degrees to the radian equivalent
- [x] [exp](https://php.net/manual/en/function.exp.php) — Calculates the
  exponent of e
- [x] [expm1](https://php.net/manual/en/function.expm1.php) — Returns
  exp(number) - 1, computed in a way that is accurate even when the value
  of number is close to zero
- [x] [floor](https://php.net/manual/en/function.floor.php) — Round
  fractions down
- [x] [fmod](https://php.net/manual/en/function.fmod.php) — Returns the
  floating point remainder (modulo) of the division of the arguments
- [ ] [getrandmax](https://php.net/manual/en/function.getrandmax.php) — Show
  largest possible random value
- [x] [hexdec](https://php.net/manual/en/function.hexdec.php) — Hexadecimal
  to decimal
- [x] [hypot](https://php.net/manual/en/function.hypot.php) — Calculate the
  length of the hypotenuse of a right-angle triangle
- [ ] [intdiv](https://php.net/manual/en/function.intdiv.php) — Integer
  division
- [x] [is_finite](https://php.net/manual/en/function.is-finite.php) — Finds
  whether a value is a legal finite number
- [x] [is_infinite](https://php.net/manual/en/function.is-infinite.php) —
  Finds whether a value is infinite
- [x] [is_nan](https://php.net/manual/en/function.is-nan.php) — Finds
  whether a value is not a number
- [ ] [lcg_value](https://php.net/manual/en/function.lcg-value.php) —
  Combined linear congruential generator
- [x] [log10](https://php.net/manual/en/function.log10.php) — Base-10
  logarithm
- [x] [log1p](https://php.net/manual/en/function.log1p.php) — Returns log(1
  \+ number), computed in a way that is accurate even when the value of
  number is close to zero
- [x] [log](https://php.net/manual/en/function.log.php) — Natural logarithm
- [ ] <strike>[max](https://php.net/manual/en/function.max.php) — Find
  highest value</strike>, `Built-in function in Python`
- [ ] <strike>[min](https://php.net/manual/en/function.min.php) — Find
  lowest value</strike>, `Built-in function in Python`
- [ ] [mt_getrandmax](https://php.net/manual/en/function.mt-getrandmax.php)
  — Show largest possible random value
- [x] [mt_rand](https://php.net/manual/en/function.mt-rand.php) — Generate a
  random value via the Mersenne Twister Random Number Generator
- [ ] [mt_srand](https://php.net/manual/en/function.mt-srand.php) — Seeds
  the Mersenne Twister Random Number Generator
- [x] [octdec](https://php.net/manual/en/function.octdec.php) — Octal to
  decimal
- [x] [pi](https://php.net/manual/en/function.pi.php) — Get value of pi
- [ ] <strike>[pow](https://php.net/manual/en/function.pow.php) —
  Exponential expression</strike>, `Built-in function in Python`
- [x] [rad2deg](https://php.net/manual/en/function.rad2deg.php) — Converts
  the radian number to the equivalent number in degrees
- [x] [rand](https://php.net/manual/en/function.rand.php) — Generate a
  random integer
- [ ] <strike>[round](https://php.net/manual/en/function.round.php) — Rounds
  a float</strike>, `Built-in function in Python`
- [x] [sin](https://php.net/manual/en/function.sin.php) — Sine
- [x] [sinh](https://php.net/manual/en/function.sinh.php) — Hyperbolic sine
- [x] [sqrt](https://php.net/manual/en/function.sqrt.php) — Square root
- [x] [srand](https://php.net/manual/en/function.srand.php) — Seed the
  random number generator
- [x] [tan](https://php.net/manual/en/function.tan.php) — Tangent
- [x] [tanh](https://php.net/manual/en/function.tanh.php) — Hyperbolic
  tangent

## Misc. Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [ ] [connection_aborted](https://php.net/manual/en/function.connection-aborted.php)
  — Check whether client disconnected
- [ ] [connection_status](https://php.net/manual/en/function.connection-status.php)
  — Returns connection status bitfield
- [ ] [constant](https://php.net/manual/en/function.constant.php) — Returns
  the value of a constant
- [ ] [define](https://php.net/manual/en/function.define.php) — Defines a
  named constant
- [ ] [defined](https://php.net/manual/en/function.defined.php) — Checks
  whether a given named constant exists
- [x] [die](https://php.net/manual/en/function.die.php) — Equivalent to exit
- [ ] <strike>[eval](https://php.net/manual/en/function.eval.php) — Evaluate
  a string as PHP code</strike>
- [ ] <strike>[exit](https://php.net/manual/en/function.exit.php) — Output a
  message and terminate the current script</strike>
- [ ] [get_browser](https://php.net/manual/en/function.get-browser.php) —
  Tells what the user's browser is capable of
- [ ] [\_\_halt_compiler](https://php.net/manual/en/function.halt-compiler.php)
  — Halts the compiler execution
- [ ] [highlight_file](https://php.net/manual/en/function.highlight-file.php)
  — Syntax highlighting of a file
- [ ] [highlight_string](https://php.net/manual/en/function.highlight-string.php)
  — Syntax highlighting of a string
- [ ] [hrtime](https://php.net/manual/en/function.hrtime.php) — Get the
  system's high resolution time
- [ ] [ignore_user_abort](https://php.net/manual/en/function.ignore-user-abort.php)
  — Set whether a client disconnect should abort script execution
- [x] [pack](https://php.net/manual/en/function.pack.php) — Pack data into
  binary string
- [ ] [php_check_syntax](https://php.net/manual/en/function.php-check-syntax.php)
  — Check the PHP syntax of (and execute) the specified file
- [ ] [php_strip_whitespace](https://php.net/manual/en/function.php-strip-whitespace.php)
  — Return source with stripped comments and whitespace
- [ ] [sapi_windows_cp_conv](https://php.net/manual/en/function.sapi-windows-cp-conv.php)
  — Convert string from one codepage to another
- [ ] [sapi_windows_cp_get](https://php.net/manual/en/function.sapi-windows-cp-get.php)
  — Get process codepage
- [ ] [sapi_windows_cp_is_utf8](https://php.net/manual/en/function.sapi-windows-cp-is-utf8.php)
  — Indicates whether the codepage is UTF-8 compatible
- [ ] [sapi_windows_cp_set](https://php.net/manual/en/function.sapi-windows-cp-set.php)
  — Set process codepage
- [ ] [sapi_windows_vt100_support](https://php.net/manual/en/function.sapi-windows-vt100-support.php)
  — Get or set VT100 support for the specified stream associated to an
  output buffer of a Windows console.
- [ ] [show_source](https://php.net/manual/en/function.show-source.php) —
  Alias of highlight_file
- [x] [sleep](https://php.net/manual/en/function.sleep.php) — Delay
  execution
- [x] [sys_getloadavg](https://php.net/manual/en/function.sys-getloadavg.php)
  — Gets system load average
- [ ] [time_nanosleep](https://php.net/manual/en/function.time-nanosleep.php)
  — Delay for a number of seconds and nanoseconds
- [x] [time_sleep_until](https://php.net/manual/en/function.time-sleep-until.php)
  — Make the script sleep until the specified time
- [x] [uniqid](https://php.net/manual/en/function.uniqid.php) — Generate a
  unique ID
- [x] [unpack](https://php.net/manual/en/function.unpack.php) — Unpack data
  from binary string
- [x] [usleep](https://php.net/manual/en/function.usleep.php) — Delay
  execution in microseconds

## Network Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [ ] [checkdnsrr](https://php.net/manual/en/function.checkdnsrr.php) —
  Check DNS records corresponding to a given Internet host name or IP
  address
- [x] [closelog](https://php.net/manual/en/function.closelog.php) — Close
  connection to system logger
- [ ] [define_syslog_variables](https://php.net/manual/en/function.define-syslog-variables.php)
  — Initializes all syslog related variables
- [ ] [dns_check_record](https://php.net/manual/en/function.dns-check-record.php)
  — Alias of checkdnsrr
- [ ] [dns_get_mx](https://php.net/manual/en/function.dns-get-mx.php) —
  Alias of getmxrr
- [ ] [dns_get_record](https://php.net/manual/en/function.dns-get-record.php)
  — Fetch DNS Resource Records associated with a hostname
- [x] [fsockopen](https://php.net/manual/en/function.fsockopen.php) — Open
  Internet or Unix domain socket connection
- [x] [gethostbyaddr](https://php.net/manual/en/function.gethostbyaddr.php)
  — Get the Internet host name corresponding to a given IP address
- [x] [gethostbyname](https://php.net/manual/en/function.gethostbyname.php)
  — Get the IPv4 address corresponding to a given Internet host name
- [x] [gethostbynamel](https://php.net/manual/en/function.gethostbynamel.php)
  — Get a list of IPv4 addresses corresponding to a given Internet host
  name
- [x] [gethostname](https://php.net/manual/en/function.gethostname.php) —
  Gets the host name
- [ ] [getmxrr](https://php.net/manual/en/function.getmxrr.php) — Get MX
  records corresponding to a given Internet host name
- [x] [getprotobyname](https://php.net/manual/en/function.getprotobyname.php)
  — Get protocol number associated with protocol name
- [x] [getprotobynumber](https://php.net/manual/en/function.getprotobynumber.php)
  — Get protocol name associated with protocol number
- [x] [getservbyname](https://php.net/manual/en/function.getservbyname.php)
  — Get port number associated with an Internet service and protocol
- [x] [getservbyport](https://php.net/manual/en/function.getservbyport.php)
  — Get Internet service which corresponds to port and protocol
- [ ] [header_register_callback](https://php.net/manual/en/function.header-register-callback.php)
  — Call a header function
- [ ] [header_remove](https://php.net/manual/en/function.header-remove.php)
  — Remove previously set headers
- [ ] [header](https://php.net/manual/en/function.header.php) — Send a raw
  HTTP header
- [ ] [headers_list](https://php.net/manual/en/function.headers-list.php) —
  Returns a list of response headers sent (or ready to send)
- [ ] [headers_sent](https://php.net/manual/en/function.headers-sent.php) —
  Checks if or where headers have been sent
- [ ] [http_response_code](https://php.net/manual/en/function.http-response-code.php)
  — Get or Set the HTTP response code
- [x] [inet_ntop](https://php.net/manual/en/function.inet-ntop.php) —
  Converts a packed internet address to a human readable representation
- [x] [inet_pton](https://php.net/manual/en/function.inet-pton.php) —
  Converts a human readable IP address to its packed in_addr representation
- [x] [ip2long](https://php.net/manual/en/function.ip2long.php) — Converts a
  string containing an (IPv4) Internet Protocol dotted address into a long
  integer
- [x] [long2ip](https://php.net/manual/en/function.long2ip.php) — Converts
  an long integer address into a string in (IPv4) Internet standard dotted
  format
- [x] [openlog](https://php.net/manual/en/function.openlog.php) — Open
  connection to system logger
- [ ] [pfsockopen](https://php.net/manual/en/function.pfsockopen.php) — Open
  persistent Internet or Unix domain socket connection
- [x] [setcookie](https://php.net/manual/en/function.setcookie.php) — Send a
  cookie
- [ ] [setrawcookie](https://php.net/manual/en/function.setrawcookie.php) —
  Send a cookie without urlencoding the cookie value
- [ ] [socket_get_status](https://php.net/manual/en/function.socket-get-status.php)
  — Alias of stream_get_meta_data
- [ ] [socket_set_blocking](https://php.net/manual/en/function.socket-set-blocking.php)
  — Alias of stream_set_blocking
- [ ] [socket_set_timeout](https://php.net/manual/en/function.socket-set-timeout.php)
  — Alias of stream_set_timeout
- [x] [syslog](https://php.net/manual/en/function.syslog.php) — Generate a
  system log message

## Program execution Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [x] [escapeshellarg](https://php.net/manual/en/function.escapeshellarg.php)
  — Escape a string to be used as a shell argument
- [ ] [escapeshellcmd](https://php.net/manual/en/function.escapeshellcmd.php)
  — Escape shell metacharacters
- [ ] <strike>[exec](https://php.net/manual/en/function.exec.php) — Execute
  an external program</strike>
- [ ] [passthru](https://php.net/manual/en/function.passthru.php) — Execute
  an external program and display raw output
- [ ] [proc_close](https://php.net/manual/en/function.proc-close.php) —
  Close a process opened by proc_open and return the exit code of that
  process
- [ ] [proc_get_status](https://php.net/manual/en/function.proc-get-status.php)
  — Get information about a process opened by proc_open
- [ ] [proc_nice](https://php.net/manual/en/function.proc-nice.php) — Change
  the priority of the current process
- [ ] [proc_open](https://php.net/manual/en/function.proc-open.php) —
  Execute a command and open file pointers for input/output
- [ ] [proc_terminate](https://php.net/manual/en/function.proc-terminate.php)
  — Kills a process opened by proc_open
- [x] [shell_exec](https://php.net/manual/en/function.shell-exec.php) —
  Execute command via shell and return the complete output as a string
- [x] [system](https://php.net/manual/en/function.system.php) — Execute an
  external program and display the output

## String Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [ ] [addcslashes](https://php.net/manual/en/function.addcslashes.php) —
  Quote string with slashes in a C style
- [ ] [addslashes](https://php.net/manual/en/function.addslashes.php) —
  Quote string with slashes
- [x] [bin2hex](https://php.net/manual/en/function.bin2hex.php) — Convert
  binary data into hexadecimal representation
- [x] [chop](https://php.net/manual/en/function.chop.php) — Alias of rtrim
- [x] <strike>[chr](https://php.net/manual/en/function.chr.php) — Generate a
  single-byte string from a number</strike>, `Built-in function in Python`
- [x] [chunk_split](https://php.net/manual/en/function.chunk-split.php) —
  Split a string into smaller chunks
- [ ] [convert_cyr_string](https://php.net/manual/en/function.convert-cyr-string.php)
  — Convert from one Cyrillic character set to another
- [ ] [convert_uudecode](https://php.net/manual/en/function.convert-uudecode.php)
  — Decode a uuencoded string
- [ ] [convert_uuencode](https://php.net/manual/en/function.convert-uuencode.php)
  — Uuencode a string
- [x] [count_chars](https://php.net/manual/en/function.count-chars.php) —
  Return information about characters used in a string
- [x] [crc32](https://php.net/manual/en/function.crc32.php) — Calculates the
  crc32 polynomial of a string
- [x] [crypt](https://php.net/manual/en/function.crypt.php) — One-way string
  hashing
- [x] [echo](https://php.net/manual/en/function.echo.php) — Output one or
  more strings
- [x] [explode](https://php.net/manual/en/function.explode.php) — Split a
  string by a string
- [ ] [fprintf](https://php.net/manual/en/function.fprintf.php) — Write a
  formatted string to a stream
- [ ] [get_html_translation_table](https://php.net/manual/en/function.get-html-translation-table.php)
  — Returns the translation table used by htmlspecialchars and htmlentities
- [ ] [hebrev](https://php.net/manual/en/function.hebrev.php) — Convert
  logical Hebrew text to visual text
- [ ] [hebrevc](https://php.net/manual/en/function.hebrevc.php) — Convert
  logical Hebrew text to visual text with newline conversion
- [x] [hex2bin](https://php.net/manual/en/function.hex2bin.php) — Decodes a
  hexadecimally encoded binary string
- [ ] [html_entity_decode](https://php.net/manual/en/function.html-entity-decode.php)
  — Convert HTML entities to their corresponding characters
- [ ] [htmlentities](https://php.net/manual/en/function.htmlentities.php) —
  Convert all applicable characters to HTML entities
- [ ] [htmlspecialchars_decode](https://php.net/manual/en/function.htmlspecialchars-decode.php)
  — Convert special HTML entities back to characters
- [ ] [htmlspecialchars](https://php.net/manual/en/function.htmlspecialchars.php)
  — Convert special characters to HTML entities
- [x] [implode](https://php.net/manual/en/function.implode.php) — Join array
  elements with a string
- [x] [join](https://php.net/manual/en/function.join.php) — Alias of implode
- [x] [lcfirst](https://php.net/manual/en/function.lcfirst.php) — Make a
  string's first character lowercase
- [x] [levenshtein](https://php.net/manual/en/function.levenshtein.php) —
  Calculate Levenshtein distance between two strings
- [ ] [localeconv](https://php.net/manual/en/function.localeconv.php) — Get
  numeric formatting information
- [x] [ltrim](https://php.net/manual/en/function.ltrim.php) — Strip
  whitespace (or other characters) from the beginning of a string
- [x] [md5_file](https://php.net/manual/en/function.md5-file.php) —
  Calculates the md5 hash of a given file
- [x] [md5](https://php.net/manual/en/function.md5.php) — Calculate the md5
  hash of a string
- [ ] [metaphone](https://php.net/manual/en/function.metaphone.php) —
  Calculate the metaphone key of a string
- [ ] [money_format](https://php.net/manual/en/function.money-format.php) —
  Formats a number as a currency string
- [ ] [nl_langinfo](https://php.net/manual/en/function.nl-langinfo.php) —
  Query language and locale information
- [x] [nl2br](https://php.net/manual/en/function.nl2br.php) — Inserts HTML
  line breaks before all newlines in a string
- [x] [number_format](https://php.net/manual/en/function.number-format.php)
  — Format a number with grouped thousands
- [ ] <strike>[ord](https://php.net/manual/en/function.ord.php) — Convert
  the first byte of a string to a value between 0 and 255</strike>,
  `Built-in function in Python`
- [ ] [parse_str](https://php.net/manual/en/function.parse-str.php) — Parses
  the string into variables
- [ ] <strike>[print](https://php.net/manual/en/function.print.php) — Output
  a string</strike>, `Built-in function in Python`
- [x] [printf](https://php.net/manual/en/function.printf.php) — Output a
  formatted string
- [ ] [quoted_printable_decode](https://php.net/manual/en/function.quoted-printable-decode.php)
  — Convert a quoted-printable string to an 8 bit string
- [ ] [quoted_printable_encode](https://php.net/manual/en/function.quoted-printable-encode.php)
  — Convert a 8 bit string to a quoted-printable string
- [ ] [quotemeta](https://php.net/manual/en/function.quotemeta.php) — Quote
  meta characters
- [x] [rtrim](https://php.net/manual/en/function.rtrim.php) — Strip
  whitespace (or other characters) from the end of a string
- [ ] [setlocale](https://php.net/manual/en/function.setlocale.php) — Set
  locale information
- [x] [sha1_file](https://php.net/manual/en/function.sha1-file.php) —
  Calculate the sha1 hash of a file
- [x] [sha1](https://php.net/manual/en/function.sha1.php) — Calculate the
  sha1 hash of a string
- [ ] [similar_text](https://php.net/manual/en/function.similar-text.php) —
  Calculate the similarity between two strings
- [ ] [soundex](https://php.net/manual/en/function.soundex.php) — Calculate
  the soundex key of a string
- [ ] [sprintf](https://php.net/manual/en/function.sprintf.php) — Return a
  formatted string
- [ ] [sscanf](https://php.net/manual/en/function.sscanf.php) — Parses input
  from a string according to a format
- [x] [str_getcsv](https://php.net/manual/en/function.str-getcsv.php) —
  Parse a CSV string into an array
- [x] [str_ireplace](https://php.net/manual/en/function.str-ireplace.php) —
  Case-insensitive version of str_replace
- [x] [str_pad](https://php.net/manual/en/function.str-pad.php) — Pad a
  string to a certain length with another string
- [x] [str_repeat](https://php.net/manual/en/function.str-repeat.php) —
  Repeat a string
- [x] [str_replace](https://php.net/manual/en/function.str-replace.php) —
  Replace all occurrences of the search string with the replacement string
- [x] [str_rot13](https://php.net/manual/en/function.str-rot13.php) —
  Perform the rot13 transform on a string
- [x] [str_shuffle](https://php.net/manual/en/function.xtr-shuffle.php) —
  Randomly shuffles a string
- [x] [str_split](https://php.net/manual/en/function.str-split.php) —
  Convert a string to an array
- [x] [str_word_count](https://php.net/manual/en/function.str-word-count.php)
  — Return information about words used in a string
- [ ] [strcasecmp](https://php.net/manual/en/function.strcasecmp.php) —
  Binary safe case-insensitive string comparison
- [x] [strchr](https://php.net/manual/en/function.strchr.php) — Alias of
  strstr
- [x] [strcmp](https://php.net/manual/en/function.strcmp.php) — Binary safe
  string comparison
- [ ] [strcoll](https://php.net/manual/en/function.strcoll.php) — Locale
  based string comparison
- [x] [strcspn](https://php.net/manual/en/function.strcspn.php) — Find
  length of initial segment not matching mask
- [ ] [strip_tags](https://php.net/manual/en/function.strip-tags.php) —
  Strip HTML and PHP tags from a string
- [ ] [stripcslashes](https://php.net/manual/en/function.stripcslashes.php)
  — Un-quote string quoted with addcslashes
- [x] [stripos](https://php.net/manual/en/function.stripos.php) — Find the
  position of the first occurrence of a case-insensitive substring in a
  string
- [ ] [stripslashes](https://php.net/manual/en/function.stripslashes.php) —
  Un-quotes a quoted string
- [x] [stristr](https://php.net/manual/en/function.stristr.php) —
  Case-insensitive strstr
- [x] [strlen](https://php.net/manual/en/function.strlen.php) — Get string
  length
- [ ] [strnatcasecmp](https://php.net/manual/en/function.strnatcasecmp.php)
  — Case insensitive string comparisons using a "natural order" algorithm
- [ ] [strnatcmp](https://php.net/manual/en/function.strnatcmp.php) — String
  comparisons using a "natural order" algorithm
- [ ] [strncasecmp](https://php.net/manual/en/function.strncasecmp.php) —
  Binary safe case-insensitive string comparison of the first n characters
- [ ] [strncmp](https://php.net/manual/en/function.strncmp.php) — Binary
  safe string comparison of the first n characters
- [x] [strpbrk](https://php.net/manual/en/function.strpbrk.php) — Search a
  string for any of a set of characters
- [x] [strpos](https://php.net/manual/en/function.strpos.php) — Find the
  position of the first occurrence of a substring in a string
- [x] [strrchr](https://php.net/manual/en/function.strrchr.php) — Find the
  last occurrence of a character in a string
- [x] [strrev](https://php.net/manual/en/function.strrev.php) — Reverse a
  string
- [x] [strripos](https://php.net/manual/en/function.strripos.php) — Find the
  position of the last occurrence of a case-insensitive substring in a
  string
- [x] [strrpos](https://php.net/manual/en/function.strrpos.php) — Find the
  position of the last occurrence of a substring in a string
- [x] [strspn](https://php.net/manual/en/function.strspn.php) — Finds the
  length of the initial segment of a string consisting entirely of
  characters contained within a given mask
- [x] [strstr](https://php.net/manual/en/function.strstr.php) — Find the
  first occurrence of a string
- [ ] [strtok](https://php.net/manual/en/function.strtok.php) — Tokenize
  string
- [x] [strtolower](https://php.net/manual/en/function.strtolower.php) — Make
  a string lowercase
- [x] [strtoupper](https://php.net/manual/en/function.strtoupper.php) — Make
  a string uppercase
- [x] [strtr](https://php.net/manual/en/function.strtr.php) — Translate
  characters or replace substrings
- [ ] [substr_compare](https://php.net/manual/en/function.substr-compare.php)
  — Binary safe comparison of two strings from an offset, up to length
  characters
- [x] [substr_count](https://php.net/manual/en/function.substr-count.php) —
  Count the number of substring occurrences
- [x] [substr_replace](https://php.net/manual/en/function.substr-replace.php)
  — Replace text within a portion of a string
- [x] [substr](https://php.net/manual/en/function.substr.php) — Return part
  of a string
- [x] [trim](https://php.net/manual/en/function.trim.php) — Strip whitespace
  (or other characters) from the beginning and end of a string
- [x] [ucfirst](https://php.net/manual/en/function.ucfirst.php) — Make a
  string's first character uppercase
- [x] [ucwords](https://php.net/manual/en/function.ucwords.php) — Uppercase
  the first character of each word in a string
- [ ] [vfprintf](https://php.net/manual/en/function.vfprintf.php) — Write a
  formatted string to a stream
- [ ] [vprintf](https://php.net/manual/en/function.vprintf.php) — Output a
  formatted string
- [ ] [vsprintf](https://php.net/manual/en/function.vsprintf.php) — Return a
  formatted string
- [x] [wordwrap](https://php.net/manual/en/function.wordwrap.php) — Wraps a
  string to a given number of characters

## URL Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [x] [base64_decode](https://php.net/manual/en/function.base64-decode.php)
  — Decodes data encoded with MIME base64
- [x] [base64_encode](https://php.net/manual/en/function.base64-encode.php)
  — Encodes data with MIME base64
- [x] [get_headers](https://php.net/manual/en/function.get-headers.php) —
  Fetches all the headers sent by the server in response to an HTTP request
- [x] [get_meta_tags](https://php.net/manual/en/function.get-meta-tags.php)
  — Extracts all meta tag content attributes from a file and returns an
  array
- [x] [http_build_query](https://php.net/manual/en/function.http-build-query.php)
  — Generate URL-encoded query string
- [x] [parse_url](https://php.net/manual/en/function.parse-url.php) — Parse
  a URL and return its components
- [x] [rawurldecode](https://php.net/manual/en/function.rawurldecode.php) —
  Decode URL-encoded strings
- [x] [rawurlencode](https://php.net/manual/en/function.rawurlencode.php) —
  URL-encode according to RFC 3986
- [x] [urldecode](https://php.net/manual/en/function.urldecode.php) —
  Decodes URL-encoded string
- [x] [urlencode](https://php.net/manual/en/function.urlencode.php) —
  URL-encodes string

## Variable handling Functions

<div align="right">
    <b><a href="#php2python">↥ back to top</a></b>
</div>

- [x] [boolval](https://php.net/manual/en/function.boolval.php) — Get the
  boolean value of a variable
- [ ] <strike>[debug_zval_dump](https://php.net/manual/en/function.debug-zval-dump.php)
  — Dumps a string representation of an internal zend value to
  output</strike>
- [x] [doubleval](https://php.net/manual/en/function.doubleval.php) — Alias
  of floatval
- [x] [empty](https://php.net/manual/en/function.empty.php) — Determine
  whether a variable is empty
- [x] [floatval](https://php.net/manual/en/function.floatval.php) — Get
  float value of a variable
- [ ] [get_defined_vars](https://php.net/manual/en/function.get-defined-vars.php)
  — Returns an array of all defined variables
- [ ] [get_resource_type](https://php.net/manual/en/function.get-resource-type.php)
  — Returns the resource type
- [x] [gettype](https://php.net/manual/en/function.gettype.php) — Get the
  type of a variable
- [ ] [import_request_variables](https://php.net/manual/en/function.import-request-variables.php)
  — Import GET/POST/Cookie variables into the global scope
- [x] [intval](https://php.net/manual/en/function.intval.php) — Get the
  integer value of a variable
- [x] [is_array](https://php.net/manual/en/function.is-array.php) — Finds
  whether a variable is an array
- [x] [is_bool](https://php.net/manual/en/function.is-bool.php) — Finds out
  whether a variable is a boolean
- [x] [is_callable](https://php.net/manual/en/function.is-callable.php) —
  Verify that the contents of a variable can be called as a function
- [x] [is_countable](https://php.net/manual/en/function.is-countable.php) —
  Verify that the contents of a variable is a countable value
- [x] [is_double](https://php.net/manual/en/function.is-double.php) — Alias
  of is_float
- [x] [is_float](https://php.net/manual/en/function.is-float.php) — Finds
  whether the type of a variable is float
- [x] [is_int](https://php.net/manual/en/function.is-int.php) — Find whether
  the type of a variable is integer
- [x] [is_integer](https://php.net/manual/en/function.is-integer.php) —
  Alias of is_int
- [x] [is_iterable](https://php.net/manual/en/function.is-iterable.php) —
  Verify that the contents of a variable is an iterable value
- [x] [is_long](https://php.net/manual/en/function.is-long.php) — Alias of
  is_int
- [x] [is_null](https://php.net/manual/en/function.is-null.php) — Finds
  whether a variable is NULL
- [x] [is_numeric](https://php.net/manual/en/function.is-numeric.php) —
  Finds whether a variable is a number or a numeric string
- [x] [is_object](https://php.net/manual/en/function.is-object.php) — Finds
  whether a variable is an object
- [x] [is_real](https://php.net/manual/en/function.is-real.php) — Alias of
  is_float
- [ ] [is_resource](https://php.net/manual/en/function.is-resource.php) —
  Finds whether a variable is a resource
- [x] [is_scalar](https://php.net/manual/en/function.is-scalar.php) — Finds
  whether a variable is a scalar
- [x] [is_string](https://php.net/manual/en/function.is-string.php) — Find
  whether the type of a variable is string
- [x] [isset](https://php.net/manual/en/function.isset.php) — Determine if a
  variable is set and is not NULL
- [x] [print_r](https://php.net/manual/en/function.print-r.php) — Prints
  human-readable information about a variable
- [x] [serialize](https://php.net/manual/en/function.serialize.php) —
  Generates a storable representation of a value
- [ ] [settype](https://php.net/manual/en/function.settype.php) — Set the
  type of a variable
- [x] [strval](https://php.net/manual/en/function.strval.php) — Get string
  value of a variable
- [ ] [unserialize](https://php.net/manual/en/function.unserialize.php) —
  Creates a PHP value from a stored representation
- [x] [unset](https://php.net/manual/en/function.unset.php) — Unset a given
  variable
- [x] [var_dump](https://php.net/manual/en/function.var-dump.php) — Dumps
  information about a variable
- [x] [var_export](https://php.net/manual/en/function.var-export.php) —
  Outputs or returns a parsable string representation of a variable
