# PHP2Python

Python alternatives for PHP internal (built-in) functions.

* [php2go](https://github.com/syyongx/php2go)
* [php2python](https://github.com/jxlwqq/php2python)

## Table of Contents
* [Array Functions](#array-functions)
* [String Functions](#string-functions)
* [Date/Time Functions](#datetime-functions) 
* [Mathematical Functions](#mathematical-functions) 
* [Variable handling Functions](#variable-handling-functions)
* [URL Functions](#url-functions) 
* [Program execution Functions](#program-execution-functions) 
* [Network Functions](#network-functions) 
* [Filesystem Functions](#filesystem-functions) 
* [Misc. Functions](#misc-functions)

## Array Functions

* [ ] [array_change_key_case](http://php.net/manual/en/function.array-change-key-case.php) — Changes the case of all keys in an array
* [ ] [array_chunk](http://php.net/manual/en/function.array-chunk.php) — Split an array into chunks
* [ ] [array_column](http://php.net/manual/en/function.array-column.php) — Return the values from a single column in the input array
* [ ] [array_combine](http://php.net/manual/en/function.array-combine.php) — Creates an array by using one array for keys and another for its values
* [ ] [array_count_values](http://php.net/manual/en/function.array-count-values.php) — Counts all the values of an array
* [ ] [array_diff_assoc](http://php.net/manual/en/function.array-diff-assoc.php) — Computes the difference of arrays with additional index check
* [ ] [array_diff_key](http://php.net/manual/en/function.array-diff-key.php) — Computes the difference of arrays using keys for comparison
* [ ] [array_diff_uassoc](http://php.net/manual/en/function.array-diff-uassoc.php) — Computes the difference of arrays with additional index check which is performed by a user supplied callback function
* [ ] [array_diff_ukey](http://php.net/manual/en/function.array-diff-ukey.php) — Computes the difference of arrays using a callback function on the keys for comparison
* [ ] [array_diff](http://php.net/manual/en/function.array-diff.php) — Computes the difference of arrays
* [ ] [array_fill_keys](http://php.net/manual/en/function.array-fill-keys.php) — Fill an array with values, specifying keys
* [ ] [array_fill](http://php.net/manual/en/function.array-fill.php) — Fill an array with values
* [ ] [array_filter](http://php.net/manual/en/function.array-filter.php) — Filters elements of an array using a callback function
* [ ] [array_flip](http://php.net/manual/en/function.array-flip.php) — Exchanges all keys with their associated values in an array
* [ ] [array_intersect_assoc](http://php.net/manual/en/function.array-intersect-assoc.php) — Computes the intersection of arrays with additional index check
* [ ] [array_intersect_key](http://php.net/manual/en/function.array-intersect-key.php) — Computes the intersection of arrays using keys for comparison
* [ ] [array_intersect_uassoc](http://php.net/manual/en/function.array-intersect-uassoc.php) — Computes the intersection of arrays with additional index check, compares indexes by a callback function
* [ ] [array_intersect_ukey](http://php.net/manual/en/function.array-intersect-ukey.php) — Computes the intersection of arrays using a callback function on the keys for comparison
* [ ] [array_intersect](http://php.net/manual/en/function.array-intersect.php) — Computes the intersection of arrays
* [ ] [array_key_exists](http://php.net/manual/en/function.array-key-exists.php) — Checks if the given key or index exists in the array
* [ ] [array_key_first](http://php.net/manual/en/function.array-key-first.php) — Gets the first key of an array
* [ ] [array_key_last](http://php.net/manual/en/function.array-key-last.php) — Gets the last key of an array
* [ ] [array_keys](http://php.net/manual/en/function.array-keys.php) — Return all the keys or a subset of the keys of an array
* [ ] [array_map](http://php.net/manual/en/function.array-map.php) — Applies the callback to the elements of the given arrays
* [ ] [array_merge_recursive](http://php.net/manual/en/function.array-merge-recursive.php) — Merge one or more arrays recursively
* [ ] [array_merge](http://php.net/manual/en/function.array-merge.php) — Merge one or more arrays
* [ ] [array_multisort](http://php.net/manual/en/function.array-multisort.php) — Sort multiple or multi-dimensional arrays
* [ ] [array_pad](http://php.net/manual/en/function.array-pad.php) — Pad array to the specified length with a value
* [ ] [array_pop](http://php.net/manual/en/function.array-pop.php) — Pop the element off the end of array
* [ ] [array_product](http://php.net/manual/en/function.array-product.php) — Calculate the product of values in an array
* [ ] [array_push](http://php.net/manual/en/function.array-push.php) — Push one or more elements onto the end of array
* [ ] [array_rand](http://php.net/manual/en/function.array-rand.php) — Pick one or more random keys out of an array
* [ ] [array_reduce](http://php.net/manual/en/function.array-reduce.php) — Iteratively reduce the array to a single value using a callback function
* [ ] [array_replace_recursive](http://php.net/manual/en/function.array-replace-recursive.php) — Replaces elements from passed arrays into the first array recursively
* [ ] [array_replace](http://php.net/manual/en/function.array-replace.php) — Replaces elements from passed arrays into the first array
* [ ] [array_reverse](http://php.net/manual/en/function.array-reverse.php) — Return an array with elements in reverse order
* [ ] [array_search](http://php.net/manual/en/function.array-search.php) — Searches the array for a given value and returns the first corresponding key if successful
* [ ] [array_shift](http://php.net/manual/en/function.array-shift.php) — Shift an element off the beginning of array
* [ ] [array_slice](http://php.net/manual/en/function.array-slice.php) — Extract a slice of the array
* [ ] [array_splice](http://php.net/manual/en/function.array-splice.php) — Remove a portion of the array and replace it with something else
* [ ] [array_sum](http://php.net/manual/en/function.array-sum.php) — Calculate the sum of values in an array
* [ ] [array_udiff_assoc](http://php.net/manual/en/function.array-udiff-assoc.php) — Computes the difference of arrays with additional index check, compares data by a callback function
* [ ] [array_udiff_uassoc](http://php.net/manual/en/function.array-udiff-uassoc.php) — Computes the difference of arrays with additional index check, compares data and indexes by a callback function
* [ ] [array_udiff](http://php.net/manual/en/function.array-udiff.php) — Computes the difference of arrays by using a callback function for data comparison
* [ ] [array_uintersect_assoc](http://php.net/manual/en/function.array-uintersect-assoc.php) — Computes the intersection of arrays with additional index check, compares data by a callback function
* [ ] [array_uintersect_uassoc](http://php.net/manual/en/function.array-uintersect-uassoc.php) — Computes the intersection of arrays with additional index check, compares data and indexes by separate callback functions
* [ ] [array_uintersect](http://php.net/manual/en/function.array-uintersect.php) — Computes the intersection of arrays, compares data by a callback function
* [ ] [array_unique](http://php.net/manual/en/function.array-unique.php) — Removes duplicate values from an array
* [ ] [array_unshift](http://php.net/manual/en/function.array-unshift.php) — Prepend one or more elements to the beginning of an array
* [ ] [array_values](http://php.net/manual/en/function.array-values.php) — Return all the values of an array
* [ ] [array_walk_recursive](http://php.net/manual/en/function.array-walk-recursive.php) — Apply a user function recursively to every member of an array
* [ ] [array_walk](http://php.net/manual/en/function.array-walk.php) — Apply a user supplied function to every member of an array
* [ ] [array](http://php.net/manual/en/function.array.php) — Create an array
* [ ] [arsort](http://php.net/manual/en/function.arsort.php) — Sort an array in reverse order and maintain index association
* [ ] [asort](http://php.net/manual/en/function.asort.php) — Sort an array and maintain index association
* [ ] [compact](http://php.net/manual/en/function.compact.php) — Create array containing variables and their values
* [ ] [count](http://php.net/manual/en/function.count.php) — Count all elements in an array, or something in an object
* [ ] [current](http://php.net/manual/en/function.current.php) — Return the current element in an array
* [ ] [each](http://php.net/manual/en/function.each.php) — Return the current key and value pair from an array and advance the array cursor
* [ ] [end](http://php.net/manual/en/function.end.php) — Set the internal pointer of an array to its last element
* [ ] [extract](http://php.net/manual/en/function.extract.php) — Import variables into the current symbol table from an array
* [ ] [in_array](http://php.net/manual/en/function.in-array.php) — Checks if a value exists in an array
* [ ] [key_exists](http://php.net/manual/en/function.key-exists.php) — Alias of array_key_exists
* [ ] [key](http://php.net/manual/en/function.key.php) — Fetch a key from an array
* [ ] [krsort](http://php.net/manual/en/function.krsort.php) — Sort an array by key in reverse order
* [ ] [ksort](http://php.net/manual/en/function.ksort.php) — Sort an array by key
* [ ] <strike>[list](http://php.net/manual/en/function.list.php) — Assign variables as if they were an array</strike>, `Built-in function in Python`
* [ ] [natcasesort](http://php.net/manual/en/function.natcasesort.php) — Sort an array using a case insensitive "natural order" algorithm
* [ ] [natsort](http://php.net/manual/en/function.natsort.php) — Sort an array using a "natural order" algorithm
* [ ] <strike>[next](http://php.net/manual/en/function.next.php) — Advance the internal pointer of an array</strike>, `Built-in function in Python`
* [ ] [pos](http://php.net/manual/en/function.pos.php) — Alias of current
* [ ] [prev](http://php.net/manual/en/function.prev.php) — Rewind the internal array pointer
* [ ] <strike>[range](http://php.net/manual/en/function.range.php) — Create an array containing a range of elements</strike>, `Built-in function in Python`
* [ ] [reset](http://php.net/manual/en/function.reset.php) — Set the internal pointer of an array to its first element
* [ ] [rsort](http://php.net/manual/en/function.rsort.php) — Sort an array in reverse order
* [ ] [shuffle](http://php.net/manual/en/function.shuffle.php) — Shuffle an array
* [ ] [sizeof](http://php.net/manual/en/function.sizeof.php) — Alias of count
* [ ] [sort](http://php.net/manual/en/function.sort.php) — Sort an array
* [ ] [uasort](http://php.net/manual/en/function.uasort.php) — Sort an array with a user-defined comparison function and maintain index association
* [ ] [uksort](http://php.net/manual/en/function.uksort.php) — Sort an array by keys using a user-defined comparison function
* [ ] [usort](http://php.net/manual/en/function.usort.php) — Sort an array by values using a user-defined comparison function


## String Functions

* [ ] [addcslashes](http://php.net/manual/en/function.addcslashes.php) — Quote string with slashes in a C style
* [ ] [addslashes](http://php.net/manual/en/function.addslashes.php) — Quote string with slashes
* [ ] [bin2hex](http://php.net/manual/en/function.bin2hex.php) — Convert binary data into hexadecimal representation
* [ ] [chop](http://php.net/manual/en/function.chop.php) — Alias of rtrim
* [ ] <strike>[chr](http://php.net/manual/en/function.chr.php) — Generate a single-byte string from a number</strike>, `Built-in function in Python`
* [ ] [chunk_split](http://php.net/manual/en/function.chunk-split.php) — Split a string into smaller chunks
* [ ] [convert_cyr_string](http://php.net/manual/en/function.convert-cyr-string.php) — Convert from one Cyrillic character set to another
* [ ] [convert_uudecode](http://php.net/manual/en/function.convert-uudecode.php) — Decode a uuencoded string
* [ ] [convert_uuencode](http://php.net/manual/en/function.convert-uuencode.php) — Uuencode a string
* [ ] [count_chars](http://php.net/manual/en/function.count-chars.php) — Return information about characters used in a string
* [ ] [crc32](http://php.net/manual/en/function.crc32.php) — Calculates the crc32 polynomial of a string
* [ ] [crypt](http://php.net/manual/en/function.crypt.php) — One-way string hashing
* [ ] [echo](http://php.net/manual/en/function.echo.php) — Output one or more strings
* [ ] [explode](http://php.net/manual/en/function.explode.php) — Split a string by a string
* [ ] [fprintf](http://php.net/manual/en/function.fprintf.php) — Write a formatted string to a stream
* [ ] [get_html_translation_table](http://php.net/manual/en/function.get-html-translation-table.php) — Returns the translation table used by htmlspecialchars and htmlentities
* [ ] [hebrev](http://php.net/manual/en/function.hebrev.php) — Convert logical Hebrew text to visual text
* [ ] [hebrevc](http://php.net/manual/en/function.hebrevc.php) — Convert logical Hebrew text to visual text with newline conversion
* [ ] [hex2bin](http://php.net/manual/en/function.hex2bin.php) — Decodes a hexadecimally encoded binary string
* [ ] [html_entity_decode](http://php.net/manual/en/function.html-entity-decode.php) — Convert HTML entities to their corresponding characters
* [ ] [htmlentities](http://php.net/manual/en/function.htmlentities.php) — Convert all applicable characters to HTML entities
* [ ] [htmlspecialchars_decode](http://php.net/manual/en/function.htmlspecialchars-decode.php) — Convert special HTML entities back to characters
* [ ] [htmlspecialchars](http://php.net/manual/en/function.htmlspecialchars.php) — Convert special characters to HTML entities
* [ ] [implode](http://php.net/manual/en/function.implode.php) — Join array elements with a string
* [ ] [join](http://php.net/manual/en/function.join.php) — Alias of implode
* [ ] [lcfirst](http://php.net/manual/en/function.lcfirst.php) — Make a string's first character lowercase
* [ ] [levenshtein](http://php.net/manual/en/function.levenshtein.php) — Calculate Levenshtein distance between two strings
* [ ] [localeconv](http://php.net/manual/en/function.localeconv.php) — Get numeric formatting information
* [ ] [ltrim](http://php.net/manual/en/function.ltrim.php) — Strip whitespace (or other characters) from the beginning of a string
* [ ] [md5_file](http://php.net/manual/en/function.md5-file.php) — Calculates the md5 hash of a given file
* [ ] [md5](http://php.net/manual/en/function.md5.php) — Calculate the md5 hash of a string
* [ ] [metaphone](http://php.net/manual/en/function.metaphone.php) — Calculate the metaphone key of a string
* [ ] [money_format](http://php.net/manual/en/function.money-format.php) — Formats a number as a currency string
* [ ] [nl_langinfo](http://php.net/manual/en/function.nl-langinfo.php) — Query language and locale information
* [ ] [nl2br](http://php.net/manual/en/function.nl2br.php) — Inserts HTML line breaks before all newlines in a string
* [ ] [number_format](http://php.net/manual/en/function.number-format.php) — Format a number with grouped thousands
* [ ] <strike>[ord](http://php.net/manual/en/function.ord.php) — Convert the first byte of a string to a value between 0 and 255</strike>, `Built-in function in Python`
* [ ] [parse_str](http://php.net/manual/en/function.parse-str.php) — Parses the string into variables
* [ ] <strike>[print](http://php.net/manual/en/function.print.php) — Output a string</strike>, `Built-in function in Python`
* [ ] [printf](http://php.net/manual/en/function.printf.php) — Output a formatted string
* [ ] [quoted_printable_decode](http://php.net/manual/en/function.quoted-printable-decode.php) — Convert a quoted-printable string to an 8 bit string
* [ ] [quoted_printable_encode](http://php.net/manual/en/function.quoted-printable-encode.php) — Convert a 8 bit string to a quoted-printable string
* [ ] [quotemeta](http://php.net/manual/en/function.quotemeta.php) — Quote meta characters
* [ ] [rtrim](http://php.net/manual/en/function.rtrim.php) — Strip whitespace (or other characters) from the end of a string
* [ ] [setlocale](http://php.net/manual/en/function.setlocale.php) — Set locale information
* [ ] [sha1_file](http://php.net/manual/en/function.sha1-file.php) — Calculate the sha1 hash of a file
* [ ] [sha1](http://php.net/manual/en/function.sha1.php) — Calculate the sha1 hash of a string
* [ ] [similar_text](http://php.net/manual/en/function.similar-text.php) — Calculate the similarity between two strings
* [ ] [soundex](http://php.net/manual/en/function.soundex.php) — Calculate the soundex key of a string
* [ ] [sprintf](http://php.net/manual/en/function.sprintf.php) — Return a formatted string
* [ ] [sscanf](http://php.net/manual/en/function.sscanf.php) — Parses input from a string according to a format
* [ ] [str_getcsv](http://php.net/manual/en/function.str-getcsv.php) — Parse a CSV string into an array
* [ ] [str_ireplace](http://php.net/manual/en/function.str-ireplace.php) — Case-insensitive version of str_replace
* [ ] [str_pad](http://php.net/manual/en/function.str-pad.php) — Pad a string to a certain length with another string
* [ ] [str_repeat](http://php.net/manual/en/function.str-repeat.php) — Repeat a string
* [ ] [str_replace](http://php.net/manual/en/function.str-replace.php) — Replace all occurrences of the search string with the replacement string
* [ ] [str_rot13](http://php.net/manual/en/function.str-rot13.php) — Perform the rot13 transform on a string
* [ ] [str_shuffle](http://php.net/manual/en/function.str-shuffle.php) — Randomly shuffles a string
* [ ] [str_split](http://php.net/manual/en/function.str-split.php) — Convert a string to an array
* [ ] [str_word_count](http://php.net/manual/en/function.str-word-count.php) — Return information about words used in a string
* [ ] [strcasecmp](http://php.net/manual/en/function.strcasecmp.php) — Binary safe case-insensitive string comparison
* [ ] [strchr](http://php.net/manual/en/function.strchr.php) — Alias of strstr
* [ ] [strcmp](http://php.net/manual/en/function.strcmp.php) — Binary safe string comparison
* [ ] [strcoll](http://php.net/manual/en/function.strcoll.php) — Locale based string comparison
* [ ] [strcspn](http://php.net/manual/en/function.strcspn.php) — Find length of initial segment not matching mask
* [ ] [strip_tags](http://php.net/manual/en/function.strip-tags.php) — Strip HTML and PHP tags from a string
* [ ] [stripcslashes](http://php.net/manual/en/function.stripcslashes.php) — Un-quote string quoted with addcslashes
* [ ] [stripos](http://php.net/manual/en/function.stripos.php) — Find the position of the first occurrence of a case-insensitive substring in a string
* [ ] [stripslashes](http://php.net/manual/en/function.stripslashes.php) — Un-quotes a quoted string
* [ ] [stristr](http://php.net/manual/en/function.stristr.php) — Case-insensitive strstr
* [ ] [strlen](http://php.net/manual/en/function.strlen.php) — Get string length
* [ ] [strnatcasecmp](http://php.net/manual/en/function.strnatcasecmp.php) — Case insensitive string comparisons using a "natural order" algorithm
* [ ] [strnatcmp](http://php.net/manual/en/function.strnatcmp.php) — String comparisons using a "natural order" algorithm
* [ ] [strncasecmp](http://php.net/manual/en/function.strncasecmp.php) — Binary safe case-insensitive string comparison of the first n characters
* [ ] [strncmp](http://php.net/manual/en/function.strncmp.php) — Binary safe string comparison of the first n characters
* [ ] [strpbrk](http://php.net/manual/en/function.strpbrk.php) — Search a string for any of a set of characters
* [ ] [strpos](http://php.net/manual/en/function.strpos.php) — Find the position of the first occurrence of a substring in a string
* [ ] [strrchr](http://php.net/manual/en/function.strrchr.php) — Find the last occurrence of a character in a string
* [ ] [strrev](http://php.net/manual/en/function.strrev.php) — Reverse a string
* [ ] [strripos](http://php.net/manual/en/function.strripos.php) — Find the position of the last occurrence of a case-insensitive substring in a string
* [ ] [strrpos](http://php.net/manual/en/function.strrpos.php) — Find the position of the last occurrence of a substring in a string
* [ ] [strspn](http://php.net/manual/en/function.strspn.php) — Finds the length of the initial segment of a string consisting entirely of characters contained within a given mask
* [ ] [strstr](http://php.net/manual/en/function.strstr.php) — Find the first occurrence of a string
* [ ] [strtok](http://php.net/manual/en/function.strtok.php) — Tokenize string
* [ ] [strtolower](http://php.net/manual/en/function.strtolower.php) — Make a string lowercase
* [ ] [strtoupper](http://php.net/manual/en/function.strtoupper.php) — Make a string uppercase
* [ ] [strtr](http://php.net/manual/en/function.strtr.php) — Translate characters or replace substrings
* [ ] [substr_compare](http://php.net/manual/en/function.substr-compare.php) — Binary safe comparison of two strings from an offset, up to length characters
* [ ] [substr_count](http://php.net/manual/en/function.substr-count.php) — Count the number of substring occurrences
* [ ] [substr_replace](http://php.net/manual/en/function.substr-replace.php) — Replace text within a portion of a string
* [ ] [substr](http://php.net/manual/en/function.substr.php) — Return part of a string
* [ ] [trim](http://php.net/manual/en/function.trim.php) — Strip whitespace (or other characters) from the beginning and end of a string
* [ ] [ucfirst](http://php.net/manual/en/function.ucfirst.php) — Make a string's first character uppercase
* [ ] [ucwords](http://php.net/manual/en/function.ucwords.php) — Uppercase the first character of each word in a string
* [ ] [vfprintf](http://php.net/manual/en/function.vfprintf.php) — Write a formatted string to a stream
* [ ] [vprintf](http://php.net/manual/en/function.vprintf.php) — Output a formatted string
* [ ] [vsprintf](http://php.net/manual/en/function.vsprintf.php) — Return a formatted string
* [ ] [wordwrap](http://php.net/manual/en/function.wordwrap.php) — Wraps a string to a given number of characters


## Date/Time Functions

* [ ] [checkdate](http://php.net/manual/en/function.checkdate.php) — Validate a Gregorian date
* [ ] [date_add](http://php.net/manual/en/function.date-add.php) — Alias of DateTime::add
* [ ] [date_create_from_format](http://php.net/manual/en/function.date-create-from-format.php) — Alias of DateTime::createFromFormat
* [ ] [date_create_immutable_from_format](http://php.net/manual/en/function.date-create-immutable-from-format.php) — Alias of DateTimeImmutable::createFromFormat
* [ ] [date_create_immutable](http://php.net/manual/en/function.date-create-immutable.php) — Alias of DateTimeImmutable::__construct
* [ ] [date_create](http://php.net/manual/en/function.date-create.php) — Alias of DateTime::__construct
* [ ] [date_date_set](http://php.net/manual/en/function.date-date-set.php) — Alias of DateTime::setDate
* [ ] [date_default_timezone_get](http://php.net/manual/en/function.date-default-timezone-get.php) — Gets the default timezone used by all date/time functions in a script
* [ ] [date_default_timezone_set](http://php.net/manual/en/function.date-default-timezone-set.php) — Sets the default timezone used by all date/time functions in a script
* [ ] [date_diff](http://php.net/manual/en/function.date-diff.php) — Alias of DateTime::diff
* [ ] [date_format](http://php.net/manual/en/function.date-format.php) — Alias of DateTime::format
* [ ] [date_get_last_errors](http://php.net/manual/en/function.date-get-last-errors.php) — Alias of DateTime::getLastErrors
* [ ] [date_interval_create_from_date_string](http://php.net/manual/en/function.date-interval-create-from-date-string.php) — Alias of DateInterval::createFromDateString
* [ ] [date_interval_format](http://php.net/manual/en/function.date-interval-format.php) — Alias of DateInterval::format
* [ ] [date_isodate_set](http://php.net/manual/en/function.date-isodate-set.php) — Alias of DateTime::setISODate
* [ ] [date_modify](http://php.net/manual/en/function.date-modify.php) — Alias of DateTime::modify
* [ ] [date_offset_get](http://php.net/manual/en/function.date-offset-get.php) — Alias of DateTime::getOffset
* [ ] [date_parse_from_format](http://php.net/manual/en/function.date-parse-from-format.php) — Get info about given date formatted according to the specified format
* [ ] [date_parse](http://php.net/manual/en/function.date-parse.php) — Returns associative array with detailed info about given date
* [ ] [date_sub](http://php.net/manual/en/function.date-sub.php) — Alias of DateTime::sub
* [ ] [date_sun_info](http://php.net/manual/en/function.date-sun-info.php) — Returns an array with information about sunset/sunrise and twilight begin/end
* [ ] [date_sunrise](http://php.net/manual/en/function.date-sunrise.php) — Returns time of sunrise for a given day and location
* [ ] [date_sunset](http://php.net/manual/en/function.date-sunset.php) — Returns time of sunset for a given day and location
* [ ] [date_time_set](http://php.net/manual/en/function.date-time-set.php) — Alias of DateTime::setTime
* [ ] [date_timestamp_get](http://php.net/manual/en/function.date-timestamp-get.php) — Alias of DateTime::getTimestamp
* [ ] [date_timestamp_set](http://php.net/manual/en/function.date-timestamp-set.php) — Alias of DateTime::setTimestamp
* [ ] [date_timezone_get](http://php.net/manual/en/function.date-timezone-get.php) — Alias of DateTime::getTimezone
* [ ] [date_timezone_set](http://php.net/manual/en/function.date-timezone-set.php) — Alias of DateTime::setTimezone
* [ ] [date](http://php.net/manual/en/function.date.php) — Format a local time/date
* [ ] [getdate](http://php.net/manual/en/function.getdate.php) — Get date/time information
* [ ] [gettimeofday](http://php.net/manual/en/function.gettimeofday.php) — Get current time
* [ ] [gmdate](http://php.net/manual/en/function.gmdate.php) — Format a GMT/UTC date/time
* [ ] [gmmktime](http://php.net/manual/en/function.gmmktime.php) — Get Unix timestamp for a GMT date
* [ ] [gmstrftime](http://php.net/manual/en/function.gmstrftime.php) — Format a GMT/UTC time/date according to locale settings
* [ ] [idate](http://php.net/manual/en/function.idate.php) — Format a local time/date as integer
* [ ] [localtime](http://php.net/manual/en/function.localtime.php) — Get the local time
* [ ] [microtime](http://php.net/manual/en/function.microtime.php) — Return current Unix timestamp with microseconds
* [ ] [mktime](http://php.net/manual/en/function.mktime.php) — Get Unix timestamp for a date
* [ ] [strftime](http://php.net/manual/en/function.strftime.php) — Format a local time/date according to locale settings
* [ ] [strptime](http://php.net/manual/en/function.strptime.php) — Parse a time/date generated with strftime
* [ ] [strtotime](http://php.net/manual/en/function.strtotime.php) — Parse about any English textual datetime description into a Unix timestamp
* [ ] [time](http://php.net/manual/en/function.time.php) — Return current Unix timestamp
* [ ] [timezone_abbreviations_list](http://php.net/manual/en/function.timezone-abbreviations-list.php) — Alias of DateTimeZone::listAbbreviations
* [ ] [timezone_identifiers_list](http://php.net/manual/en/function.timezone-identifiers-list.php) — Alias of DateTimeZone::listIdentifiers
* [ ] [timezone_location_get](http://php.net/manual/en/function.timezone-location-get.php) — Alias of DateTimeZone::getLocation
* [ ] [timezone_name_from_abbr](http://php.net/manual/en/function.timezone-name-from-abbr.php) — Returns the timezone name from abbreviation
* [ ] [timezone_name_get](http://php.net/manual/en/function.timezone-name-get.php) — Alias of DateTimeZone::getName
* [ ] [timezone_offset_get](http://php.net/manual/en/function.timezone-offset-get.php) — Alias of DateTimeZone::getOffset
* [ ] [timezone_open](http://php.net/manual/en/function.timezone-open.php) — Alias of DateTimeZone::__construct
* [ ] [timezone_transitions_get](http://php.net/manual/en/function.timezone-transitions-get.php) — Alias of DateTimeZone::getTransitions
* [ ] [timezone_version_get](http://php.net/manual/en/function.timezone-version-get.php) — Gets the version of the timezonedb

## Mathematical Functions

* [ ] <strike>[abs](http://php.net/manual/en/function.abs.php) — Absolute value</strike>, `Built-in function in Python`
* [x] [acos](http://php.net/manual/en/function.acos.php) — Arc cosine
* [x] [acosh](http://php.net/manual/en/function.acosh.php) — Inverse hyperbolic cosine
* [x] [asin](http://php.net/manual/en/function.asin.php) — Arc sine
* [x] [asinh](http://php.net/manual/en/function.asinh.php) — Inverse hyperbolic sine
* [x] [atan2](http://php.net/manual/en/function.atan2.php) — Arc tangent of two variables
* [x] [atan](http://php.net/manual/en/function.atan.php) — Arc tangent
* [x] [atanh](http://php.net/manual/en/function.atanh.php) — Inverse hyperbolic tangent
* [x] [base_convert](http://php.net/manual/en/function.base-convert.php) — Convert a number between arbitrary bases
* [x] [bindec](http://php.net/manual/en/function.bindec.php) — Binary to decimal
* [x] [ceil](http://php.net/manual/en/function.ceil.php) — Round fractions up
* [x] [cos](http://php.net/manual/en/function.cos.php) — Cosine
* [x] [cosh](http://php.net/manual/en/function.cosh.php) — Hyperbolic cosine
* [x] [decbin](http://php.net/manual/en/function.decbin.php) — Decimal to binary
* [x] [dechex](http://php.net/manual/en/function.dechex.php) — Decimal to hexadecimal
* [x] [decoct](http://php.net/manual/en/function.decoct.php) — Decimal to octal
* [x] [deg2rad](http://php.net/manual/en/function.deg2rad.php) — Converts the number in degrees to the radian equivalent
* [x] [exp](http://php.net/manual/en/function.exp.php) — Calculates the exponent of e
* [x] [expm1](http://php.net/manual/en/function.expm1.php) — Returns exp(number) - 1, computed in a way that is accurate even when the value of number is close to zero
* [x] [floor](http://php.net/manual/en/function.floor.php) — Round fractions down
* [x] [fmod](http://php.net/manual/en/function.fmod.php) — Returns the floating point remainder (modulo) of the division of the arguments
* [ ] [getrandmax](http://php.net/manual/en/function.getrandmax.php) — Show largest possible random value
* [x] [hexdec](http://php.net/manual/en/function.hexdec.php) — Hexadecimal to decimal
* [x] [hypot](http://php.net/manual/en/function.hypot.php) — Calculate the length of the hypotenuse of a right-angle triangle
* [ ] [intdiv](http://php.net/manual/en/function.intdiv.php) — Integer division
* [x] [is_finite](http://php.net/manual/en/function.is-finite.php) — Finds whether a value is a legal finite number
* [x] [is_infinite](http://php.net/manual/en/function.is-infinite.php) — Finds whether a value is infinite
* [x] [is_nan](http://php.net/manual/en/function.is-nan.php) — Finds whether a value is not a number
* [ ] [lcg_value](http://php.net/manual/en/function.lcg-value.php) — Combined linear congruential generator
* [x] [log10](http://php.net/manual/en/function.log10.php) — Base-10 logarithm
* [x] [log1p](http://php.net/manual/en/function.log1p.php) — Returns log(1 + number), computed in a way that is accurate even when the value of number is close to zero
* [x] [log](http://php.net/manual/en/function.log.php) — Natural logarithm
* [ ] <strike>[max](http://php.net/manual/en/function.max.php) — Find highest value</strike>, `Built-in function in Python`
* [ ] <strike>[min](http://php.net/manual/en/function.min.php) — Find lowest value</strike>, `Built-in function in Python`
* [ ] [mt_getrandmax](http://php.net/manual/en/function.mt-getrandmax.php) — Show largest possible random value
* [ ] [mt_rand](http://php.net/manual/en/function.mt-rand.php) — Generate a random value via the Mersenne Twister Random Number Generator
* [ ] [mt_srand](http://php.net/manual/en/function.mt-srand.php) — Seeds the Mersenne Twister Random Number Generator
* [x] [octdec](http://php.net/manual/en/function.octdec.php) — Octal to decimal
* [x] [pi](http://php.net/manual/en/function.pi.php) — Get value of pi
* [ ] <strike>[pow](http://php.net/manual/en/function.pow.php) — Exponential expression</strike>, `Built-in function in Python`
* [x] [rad2deg](http://php.net/manual/en/function.rad2deg.php) — Converts the radian number to the equivalent number in degrees
* [x] [rand](http://php.net/manual/en/function.rand.php) — Generate a random integer
* [ ] <strike>[round](http://php.net/manual/en/function.round.php) — Rounds a float</strike>, `Built-in function in Python`
* [x] [sin](http://php.net/manual/en/function.sin.php) — Sine
* [x] [sinh](http://php.net/manual/en/function.sinh.php) — Hyperbolic sine
* [x] [sqrt](http://php.net/manual/en/function.sqrt.php) — Square root
* [x] [srand](http://php.net/manual/en/function.srand.php) — Seed the random number generator
* [x] [tan](http://php.net/manual/en/function.tan.php) — Tangent
* [x] [tanh](http://php.net/manual/en/function.tanh.php) — Hyperbolic tangent

## Variable handling Functions

* [x] [boolval](http://php.net/manual/en/function.boolval.php) — Get the boolean value of a variable
* [ ] [debug_zval_dump](http://php.net/manual/en/function.debug-zval-dump.php) — Dumps a string representation of an internal zend value to output
* [x] [doubleval](http://php.net/manual/en/function.doubleval.php) — Alias of floatval
* [x] [empty](http://php.net/manual/en/function.empty.php) — Determine whether a variable is empty
* [x] [floatval](http://php.net/manual/en/function.floatval.php) — Get float value of a variable
* [ ] [get_defined_vars](http://php.net/manual/en/function.get-defined-vars.php) — Returns an array of all defined variables
* [ ] [get_resource_type](http://php.net/manual/en/function.get-resource-type.php) — Returns the resource type
* [x] [gettype](http://php.net/manual/en/function.gettype.php) — Get the type of a variable
* [ ] [import_request_variables](http://php.net/manual/en/function.import-request-variables.php) — Import GET/POST/Cookie variables into the global scope
* [x] [intval](http://php.net/manual/en/function.intval.php) — Get the integer value of a variable
* [x] [is_array](http://php.net/manual/en/function.is-array.php) — Finds whether a variable is an array
* [x] [is_bool](http://php.net/manual/en/function.is-bool.php) — Finds out whether a variable is a boolean
* [ ] [is_callable](http://php.net/manual/en/function.is-callable.php) — Verify that the contents of a variable can be called as a function
* [ ] [is_countable](http://php.net/manual/en/function.is-countable.php) — Verify that the contents of a variable is a countable value
* [x] [is_double](http://php.net/manual/en/function.is-double.php) — Alias of is_float
* [x] [is_float](http://php.net/manual/en/function.is-float.php) — Finds whether the type of a variable is float
* [x] [is_int](http://php.net/manual/en/function.is-int.php) — Find whether the type of a variable is integer
* [x] [is_integer](http://php.net/manual/en/function.is-integer.php) — Alias of is_int
* [ ] [is_iterable](http://php.net/manual/en/function.is-iterable.php) — Verify that the contents of a variable is an iterable value
* [ ] [is_long](http://php.net/manual/en/function.is-long.php) — Alias of is_int
* [x] [is_null](http://php.net/manual/en/function.is-null.php) — Finds whether a variable is NULL
* [x] [is_numeric](http://php.net/manual/en/function.is-numeric.php) — Finds whether a variable is a number or a numeric string
* [x] [is_object](http://php.net/manual/en/function.is-object.php) — Finds whether a variable is an object
* [x] [is_real](http://php.net/manual/en/function.is-real.php) — Alias of is_float
* [ ] [is_resource](http://php.net/manual/en/function.is-resource.php) — Finds whether a variable is a resource
* [x] [is_scalar](http://php.net/manual/en/function.is-scalar.php) — Finds whether a variable is a scalar
* [x] [is_string](http://php.net/manual/en/function.is-string.php) — Find whether the type of a variable is string
* [x] [isset](http://php.net/manual/en/function.isset.php) — Determine if a variable is set and is not NULL
* [x] [print_r](http://php.net/manual/en/function.print-r.php) — Prints human-readable information about a variable
* [x] [serialize](http://php.net/manual/en/function.serialize.php) — Generates a storable representation of a value
* [ ] [settype](http://php.net/manual/en/function.settype.php) — Set the type of a variable
* [x] [strval](http://php.net/manual/en/function.strval.php) — Get string value of a variable
* [ ] [unserialize](http://php.net/manual/en/function.unserialize.php) — Creates a PHP value from a stored representation
* [x] [unset](http://php.net/manual/en/function.unset.php) — Unset a given variable
* [x] [var_dump](http://php.net/manual/en/function.var-dump.php) — Dumps information about a variable
* [x] [var_export](http://php.net/manual/en/function.var-export.php) — Outputs or returns a parsable string representation of a variable

## URL Functions

* [ ] [base64_decode](http://php.net/manual/en/function.base64-decode.php) — Decodes data encoded with MIME base64
* [ ] [base64_encode](http://php.net/manual/en/function.base64-encode.php) — Encodes data with MIME base64
* [ ] [get_headers](http://php.net/manual/en/function.get-headers.php) — Fetches all the headers sent by the server in response to an HTTP request
* [ ] [get_meta_tags](http://php.net/manual/en/function.get-meta-tags.php) — Extracts all meta tag content attributes from a file and returns an array
* [ ] [http_build_query](http://php.net/manual/en/function.http-build-query.php) — Generate URL-encoded query string
* [ ] [parse_url](http://php.net/manual/en/function.parse-url.php) — Parse a URL and return its components
* [ ] [rawurldecode](http://php.net/manual/en/function.rawurldecode.php) — Decode URL-encoded strings
* [ ] [rawurlencode](http://php.net/manual/en/function.rawurlencode.php) — URL-encode according to RFC 3986
* [ ] [urldecode](http://php.net/manual/en/function.urldecode.php) — Decodes URL-encoded string
* [ ] [urlencode](http://php.net/manual/en/function.urlencode.php) — URL-encodes string

## Program execution Functions

* [ ] [escapeshellarg](http://php.net/manual/en/function.escapeshellarg.php) — Escape a string to be used as a shell argument
* [ ] [escapeshellcmd](http://php.net/manual/en/function.escapeshellcmd.php) — Escape shell metacharacters
* [ ] [exec](http://php.net/manual/en/function.exec.php) — Execute an external program
* [ ] [passthru](http://php.net/manual/en/function.passthru.php) — Execute an external program and display raw output
* [ ] [proc_close](http://php.net/manual/en/function.proc-close.php) — Close a process opened by proc_open and return the exit code of that process
* [ ] [proc_get_status](http://php.net/manual/en/function.proc-get-status.php) — Get information about a process opened by proc_open
* [ ] [proc_nice](http://php.net/manual/en/function.proc-nice.php) — Change the priority of the current process
* [ ] [proc_open](http://php.net/manual/en/function.proc-open.php) — Execute a command and open file pointers for input/output
* [ ] [proc_terminate](http://php.net/manual/en/function.proc-terminate.php) — Kills a process opened by proc_open
* [ ] [shell_exec](http://php.net/manual/en/function.shell-exec.php) — Execute command via shell and return the complete output as a string
* [ ] [system](http://php.net/manual/en/function.system.php) — Execute an external program and display the output

## Network Functions

* [ ] [checkdnsrr](http://php.net/manual/en/function.checkdnsrr.php) — Check DNS records corresponding to a given Internet host name or IP address
* [ ] [closelog](http://php.net/manual/en/function.closelog.php) — Close connection to system logger
* [ ] [define_syslog_variables](http://php.net/manual/en/function.define-syslog-variables.php) — Initializes all syslog related variables
* [ ] [dns_check_record](http://php.net/manual/en/function.dns-check-record.php) — Alias of checkdnsrr
* [ ] [dns_get_mx](http://php.net/manual/en/function.dns-get-mx.php) — Alias of getmxrr
* [ ] [dns_get_record](http://php.net/manual/en/function.dns-get-record.php) — Fetch DNS Resource Records associated with a hostname
* [ ] [fsockopen](http://php.net/manual/en/function.fsockopen.php) — Open Internet or Unix domain socket connection
* [ ] [gethostbyaddr](http://php.net/manual/en/function.gethostbyaddr.php) — Get the Internet host name corresponding to a given IP address
* [ ] [gethostbyname](http://php.net/manual/en/function.gethostbyname.php) — Get the IPv4 address corresponding to a given Internet host name
* [ ] [gethostbynamel](http://php.net/manual/en/function.gethostbynamel.php) — Get a list of IPv4 addresses corresponding to a given Internet host name
* [ ] [gethostname](http://php.net/manual/en/function.gethostname.php) — Gets the host name
* [ ] [getmxrr](http://php.net/manual/en/function.getmxrr.php) — Get MX records corresponding to a given Internet host name
* [ ] [getprotobyname](http://php.net/manual/en/function.getprotobyname.php) — Get protocol number associated with protocol name
* [ ] [getprotobynumber](http://php.net/manual/en/function.getprotobynumber.php) — Get protocol name associated with protocol number
* [ ] [getservbyname](http://php.net/manual/en/function.getservbyname.php) — Get port number associated with an Internet service and protocol
* [ ] [getservbyport](http://php.net/manual/en/function.getservbyport.php) — Get Internet service which corresponds to port and protocol
* [ ] [header_register_callback](http://php.net/manual/en/function.header-register-callback.php) — Call a header function
* [ ] [header_remove](http://php.net/manual/en/function.header-remove.php) — Remove previously set headers
* [ ] [header](http://php.net/manual/en/function.header.php) — Send a raw HTTP header
* [ ] [headers_list](http://php.net/manual/en/function.headers-list.php) — Returns a list of response headers sent (or ready to send)
* [ ] [headers_sent](http://php.net/manual/en/function.headers-sent.php) — Checks if or where headers have been sent
* [ ] [http_response_code](http://php.net/manual/en/function.http-response-code.php) — Get or Set the HTTP response code
* [ ] [inet_ntop](http://php.net/manual/en/function.inet-ntop.php) — Converts a packed internet address to a human readable representation
* [ ] [inet_pton](http://php.net/manual/en/function.inet-pton.php) — Converts a human readable IP address to its packed in_addr representation
* [ ] [ip2long](http://php.net/manual/en/function.ip2long.php) — Converts a string containing an (IPv4) Internet Protocol dotted address into a long integer
* [ ] [long2ip](http://php.net/manual/en/function.long2ip.php) — Converts an long integer address into a string in (IPv4) Internet standard dotted format
* [ ] [openlog](http://php.net/manual/en/function.openlog.php) — Open connection to system logger
* [ ] [pfsockopen](http://php.net/manual/en/function.pfsockopen.php) — Open persistent Internet or Unix domain socket connection
* [ ] [setcookie](http://php.net/manual/en/function.setcookie.php) — Send a cookie
* [ ] [setrawcookie](http://php.net/manual/en/function.setrawcookie.php) — Send a cookie without urlencoding the cookie value
* [ ] [socket_get_status](http://php.net/manual/en/function.socket-get-status.php) — Alias of stream_get_meta_data
* [ ] [socket_set_blocking](http://php.net/manual/en/function.socket-set-blocking.php) — Alias of stream_set_blocking
* [ ] [socket_set_timeout](http://php.net/manual/en/function.socket-set-timeout.php) — Alias of stream_set_timeout
* [ ] [syslog](http://php.net/manual/en/function.syslog.php) — Generate a system log message

## Filesystem Functions

* [ ] [basename](http://php.net/manual/en/function.basename.php) — Returns trailing name component of path
* [ ] [chgrp](http://php.net/manual/en/function.chgrp.php) — Changes file group
* [ ] [chmod](http://php.net/manual/en/function.chmod.php) — Changes file mode
* [ ] [chown](http://php.net/manual/en/function.chown.php) — Changes file owner
* [ ] [clearstatcache](http://php.net/manual/en/function.clearstatcache.php) — Clears file status cache
* [ ] [copy](http://php.net/manual/en/function.copy.php) — Copies file
* [ ] [delete](http://php.net/manual/en/function.delete.php) — See unlink or unset
* [ ] [dirname](http://php.net/manual/en/function.dirname.php) — Returns a parent directory's path
* [ ] [disk_free_space](http://php.net/manual/en/function.disk-free-space.php) — Returns available space on filesystem or disk partition
* [ ] [disk_total_space](http://php.net/manual/en/function.disk-total-space.php) — Returns the total size of a filesystem or disk partition
* [ ] [diskfreespace](http://php.net/manual/en/function.diskfreespace.php) — Alias of disk_free_space
* [ ] [fclose](http://php.net/manual/en/function.fclose.php) — Closes an open file pointer
* [ ] [feof](http://php.net/manual/en/function.feof.php) — Tests for end-of-file on a file pointer
* [ ] [fflush](http://php.net/manual/en/function.fflush.php) — Flushes the output to a file
* [ ] [fgetc](http://php.net/manual/en/function.fgetc.php) — Gets character from file pointer
* [ ] [fgetcsv](http://php.net/manual/en/function.fgetcsv.php) — Gets line from file pointer and parse for CSV fields
* [ ] [fgets](http://php.net/manual/en/function.fgets.php) — Gets line from file pointer
* [ ] [fgetss](http://php.net/manual/en/function.fgetss.php) — Gets line from file pointer and strip HTML tags
* [ ] [file_exists](http://php.net/manual/en/function.file-exists.php) — Checks whether a file or directory exists
* [ ] [file_get_contents](http://php.net/manual/en/function.file-get-contents.php) — Reads entire file into a string
* [ ] [file_put_contents](http://php.net/manual/en/function.file-put-contents.php) — Write data to a file
* [ ] [file](http://php.net/manual/en/function.file.php) — Reads entire file into an array
* [ ] [fileatime](http://php.net/manual/en/function.fileatime.php) — Gets last access time of file
* [ ] [filectime](http://php.net/manual/en/function.filectime.php) — Gets inode change time of file
* [ ] [filegroup](http://php.net/manual/en/function.filegroup.php) — Gets file group
* [ ] [fileinode](http://php.net/manual/en/function.fileinode.php) — Gets file inode
* [ ] [filemtime](http://php.net/manual/en/function.filemtime.php) — Gets file modification time
* [ ] [fileowner](http://php.net/manual/en/function.fileowner.php) — Gets file owner
* [ ] [fileperms](http://php.net/manual/en/function.fileperms.php) — Gets file permissions
* [ ] [filesize](http://php.net/manual/en/function.filesize.php) — Gets file size
* [ ] [filetype](http://php.net/manual/en/function.filetype.php) — Gets file type
* [ ] [flock](http://php.net/manual/en/function.flock.php) — Portable advisory file locking
* [ ] [fnmatch](http://php.net/manual/en/function.fnmatch.php) — Match filename against a pattern
* [ ] [fopen](http://php.net/manual/en/function.fopen.php) — Opens file or URL
* [ ] [fpassthru](http://php.net/manual/en/function.fpassthru.php) — Output all remaining data on a file pointer
* [ ] [fputcsv](http://php.net/manual/en/function.fputcsv.php) — Format line as CSV and write to file pointer
* [ ] [fputs](http://php.net/manual/en/function.fputs.php) — Alias of fwrite
* [ ] [fread](http://php.net/manual/en/function.fread.php) — Binary-safe file read
* [ ] [fscanf](http://php.net/manual/en/function.fscanf.php) — Parses input from a file according to a format
* [ ] [fseek](http://php.net/manual/en/function.fseek.php) — Seeks on a file pointer
* [ ] [fstat](http://php.net/manual/en/function.fstat.php) — Gets information about a file using an open file pointer
* [ ] [ftell](http://php.net/manual/en/function.ftell.php) — Returns the current position of the file read/write pointer
* [ ] [ftruncate](http://php.net/manual/en/function.ftruncate.php) — Truncates a file to a given length
* [ ] [fwrite](http://php.net/manual/en/function.fwrite.php) — Binary-safe file write
* [ ] [glob](http://php.net/manual/en/function.glob.php) — Find pathnames matching a pattern
* [ ] [is_dir](http://php.net/manual/en/function.is-dir.php) — Tells whether the filename is a directory
* [ ] [is_executable](http://php.net/manual/en/function.is-executable.php) — Tells whether the filename is executable
* [ ] [is_file](http://php.net/manual/en/function.is-file.php) — Tells whether the filename is a regular file
* [ ] [is_link](http://php.net/manual/en/function.is-link.php) — Tells whether the filename is a symbolic link
* [ ] [is_readable](http://php.net/manual/en/function.is-readable.php) — Tells whether a file exists and is readable
* [ ] [is_uploaded_file](http://php.net/manual/en/function.is-uploaded-file.php) — Tells whether the file was uploaded via HTTP POST
* [ ] [is_writable](http://php.net/manual/en/function.is-writable.php) — Tells whether the filename is writable
* [ ] [is_writeable](http://php.net/manual/en/function.is-writeable.php) — Alias of is_writable
* [ ] [lchgrp](http://php.net/manual/en/function.lchgrp.php) — Changes group ownership of symlink
* [ ] [lchown](http://php.net/manual/en/function.lchown.php) — Changes user ownership of symlink
* [ ] [link](http://php.net/manual/en/function.link.php) — Create a hard link
* [ ] [linkinfo](http://php.net/manual/en/function.linkinfo.php) — Gets information about a link
* [ ] [lstat](http://php.net/manual/en/function.lstat.php) — Gives information about a file or symbolic link
* [ ] [mkdir](http://php.net/manual/en/function.mkdir.php) — Makes directory
* [ ] [move_uploaded_file](http://php.net/manual/en/function.move-uploaded-file.php) — Moves an uploaded file to a new location
* [ ] [parse_ini_file](http://php.net/manual/en/function.parse-ini-file.php) — Parse a configuration file
* [ ] [parse_ini_string](http://php.net/manual/en/function.parse-ini-string.php) — Parse a configuration string
* [ ] [pathinfo](http://php.net/manual/en/function.pathinfo.php) — Returns information about a file path
* [ ] [pclose](http://php.net/manual/en/function.pclose.php) — Closes process file pointer
* [ ] [popen](http://php.net/manual/en/function.popen.php) — Opens process file pointer
* [ ] [readfile](http://php.net/manual/en/function.readfile.php) — Outputs a file
* [ ] [readlink](http://php.net/manual/en/function.readlink.php) — Returns the target of a symbolic link
* [ ] [realpath_cache_get](http://php.net/manual/en/function.realpath-cache-get.php) — Get realpath cache entries
* [ ] [realpath_cache_size](http://php.net/manual/en/function.realpath-cache-size.php) — Get realpath cache size
* [ ] [realpath](http://php.net/manual/en/function.realpath.php) — Returns canonicalized absolute pathname
* [ ] [rename](http://php.net/manual/en/function.rename.php) — Renames a file or directory
* [ ] [rewind](http://php.net/manual/en/function.rewind.php) — Rewind the position of a file pointer
* [ ] [rmdir](http://php.net/manual/en/function.rmdir.php) — Removes directory
* [ ] [set_file_buffer](http://php.net/manual/en/function.set-file-buffer.php) — Alias of stream_set_write_buffer
* [ ] [stat](http://php.net/manual/en/function.stat.php) — Gives information about a file
* [ ] [symlink](http://php.net/manual/en/function.symlink.php) — Creates a symbolic link
* [ ] [tempnam](http://php.net/manual/en/function.tempnam.php) — Create file with unique file name
* [ ] [tmpfile](http://php.net/manual/en/function.tmpfile.php) — Creates a temporary file
* [ ] [touch](http://php.net/manual/en/function.touch.php) — Sets access and modification time of file
* [ ] [umask](http://php.net/manual/en/function.umask.php) — Changes the current umask
* [ ] [unlink](http://php.net/manual/en/function.unlink.php) — Deletes a file

## Misc. Functions

* [ ] [connection_aborted](http://php.net/manual/en/function.connection-aborted.php) — Check whether client disconnected
* [ ] [connection_status](http://php.net/manual/en/function.connection-status.php) — Returns connection status bitfield
* [ ] [constant](http://php.net/manual/en/function.constant.php) — Returns the value of a constant
* [ ] [define](http://php.net/manual/en/function.define.php) — Defines a named constant
* [ ] [defined](http://php.net/manual/en/function.defined.php) — Checks whether a given named constant exists
* [ ] [die](http://php.net/manual/en/function.die.php) — Equivalent to exit
* [ ] [eval](http://php.net/manual/en/function.eval.php) — Evaluate a string as PHP code
* [ ] [exit](http://php.net/manual/en/function.exit.php) — Output a message and terminate the current script
* [ ] [get_browser](http://php.net/manual/en/function.get-browser.php) — Tells what the user's browser is capable of
* [ ] [__halt_compiler](http://php.net/manual/en/function.halt-compiler.php) — Halts the compiler execution
* [ ] [highlight_file](http://php.net/manual/en/function.highlight-file.php) — Syntax highlighting of a file
* [ ] [highlight_string](http://php.net/manual/en/function.highlight-string.php) — Syntax highlighting of a string
* [ ] [hrtime](http://php.net/manual/en/function.hrtime.php) — Get the system's high resolution time
* [ ] [ignore_user_abort](http://php.net/manual/en/function.ignore-user-abort.php) — Set whether a client disconnect should abort script execution
* [ ] [pack](http://php.net/manual/en/function.pack.php) — Pack data into binary string
* [ ] [php_check_syntax](http://php.net/manual/en/function.php-check-syntax.php) — Check the PHP syntax of (and execute) the specified file
* [ ] [php_strip_whitespace](http://php.net/manual/en/function.php-strip-whitespace.php) — Return source with stripped comments and whitespace
* [ ] [sapi_windows_cp_conv](http://php.net/manual/en/function.sapi-windows-cp-conv.php) — Convert string from one codepage to another
* [ ] [sapi_windows_cp_get](http://php.net/manual/en/function.sapi-windows-cp-get.php) — Get process codepage
* [ ] [sapi_windows_cp_is_utf8](http://php.net/manual/en/function.sapi-windows-cp-is-utf8.php) — Indicates whether the codepage is UTF-8 compatible
* [ ] [sapi_windows_cp_set](http://php.net/manual/en/function.sapi-windows-cp-set.php) — Set process codepage
* [ ] [sapi_windows_vt100_support](http://php.net/manual/en/function.sapi-windows-vt100-support.php) — Get or set VT100 support for the specified stream associated to an output buffer of a Windows console.
* [ ] [show_source](http://php.net/manual/en/function.show-source.php) — Alias of highlight_file
* [ ] [sleep](http://php.net/manual/en/function.sleep.php) — Delay execution
* [ ] [sys_getloadavg](http://php.net/manual/en/function.sys-getloadavg.php) — Gets system load average
* [ ] [time_nanosleep](http://php.net/manual/en/function.time-nanosleep.php) — Delay for a number of seconds and nanoseconds
* [ ] [time_sleep_until](http://php.net/manual/en/function.time-sleep-until.php) — Make the script sleep until the specified time
* [ ] [uniqid](http://php.net/manual/en/function.uniqid.php) — Generate a unique ID
* [ ] [unpack](http://php.net/manual/en/function.unpack.php) — Unpack data from binary string
* [ ] [usleep](http://php.net/manual/en/function.usleep.php) — Delay execution in microseconds