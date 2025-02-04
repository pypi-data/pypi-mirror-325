pip install JynPopMod

### Utility Functions:
1. **`wait(key="s", num=1)`**: Pauses execution for a specified amount of time. The unit is controlled by the `key` parameter, which can be 's' for seconds, 'm' for minutes, or 'h' for hours.
   
2. **`ifnull(_v, _d)`**: Returns `_d` if `_v` is `None` or an empty string. Otherwise, it returns `_v`.

3. **`switch_case(_v, _c, d=None)`**: Looks up a value `_v` in dictionary `_c` and returns the corresponding value. If `_v` isn't in `_c`, it returns `d`. If the value is callable (e.g., a function), it is executed.

4. **`timer_function(func, seconds)`**: Executes the function `func` after waiting for a specified number of seconds.

5. **`iftrue(var, function)`**: If `var` is `True`, it calls the function `function`.

6. **`iffalse(var, function)`**: If `var` is `False`, it calls the function `function`.

7. **`replace(string, replacement, replacement_with)`**: Replaces occurrences of `replacement` in the string with `replacement_with`.

8. **`until(function, whattodo)`**: Repeatedly executes `whattodo()` until `function()` evaluates to `True`.

9. **`repeat(function, times)`**: Executes the function `function` a specified number of times.

10. **`oncondit(condition, function_true, function_false)`**: Executes `function_true` if `condition` is `True`, else it executes `function_false`.

11. **`repeat_forever(function)`**: Continuously executes `function` indefinitely.

12. **`safe_run(func, *args, **kwargs)`**: Safely runs a function `func`, catching and printing any exceptions that may occur.

13. **`start_timer(seconds, callback)`**: Calls `callback` after waiting for `seconds` seconds.

14. **`generate_random_string(length=15)`**: Generates a random string of alphanumeric characters and symbols of the specified `length`.

15. **`get_ip_address()`**: Returns the local IP address of the machine.

16. **`send_email(subject, body, to_email, mailname, mailpass)`**: Sends an email using Gmail's SMTP server. Requires a Gmail account's username and password.

17. **`generate_unique_id()`**: Generates and returns a unique ID using `uuid`.

18. **`start_background_task(backtask)`**: Starts a function `backtask` in a separate thread, allowing it to run in the background.

19. **`nocrash(func)`**: A decorator that wraps a function `func` to ensure it doesn't crash. If an error occurs, it is caught and logged.

20. **`parallel(*functions)`**: Executes multiple functions in parallel by running them in separate threads.

21. **`gs(func)`**: Returns the source code of the function `func` as a string.

### String and Binary Functions:
22. **`Jctb(input_string)`**: Converts a string into its binary representation, where each character is represented by a 10-bit binary value.

23. **`Jbtc(binary_input)`**: Converts a binary string (produced by `Jctb`) back to its original string.

24. **`encode_base64(data)`**: Encodes a string `data` into its Base64 representation.

25. **`decode_base64(encoded_data)`**: Decodes a Base64 encoded string back to its original string.

26. **`reverse_string(string)`**: Reverses the input string.

### Math and List Functions:
27. **`calculate_factorial(number)`**: Recursively calculates the factorial of a number.

28. **`generate_random_string(length=15)`**: (Defined twice, see above.)

29. **`swap_values(a, b)`**: Swaps the values of `a` and `b` and returns the swapped values.

30. **`replace(string, old, new)`**: (Defined twice, see above.)

31. **`find_maximum(numbers)`**: Finds and returns the maximum value in a list of numbers.

32. **`find_minimum(numbers)`**: Finds and returns the minimum value in a list of numbers.

33. **`sum_list(lst)`**: Returns the sum of elements in the list `lst`.

34. **`reverse_list(lst)`**: Returns the reverse of the list `lst`.

35. **`is_prime(n)`**: Returns `True` if `n` is a prime number, otherwise returns `False`.

36. **`split_into_chunks(text, chunk_size)`**: Splits a string `text` into chunks of size `chunk_size`.

37. **`unique_elements(lst)`**: Returns a list of unique elements from the input list `lst`.

38. **`calculate_average(numbers)`**: Returns the average of a list of numbers.

39. **`calculate_median(numbers)`**: Returns the median of a list of numbers.

40. **`count_words(text)`**: Counts and returns the number of words in the input string `text`.

41. **`count_sentences(text)`**: Counts and returns the number of sentences in the input string `text`.

42. **`add_commas(input_string)`**: Adds commas between characters in the input string.

43. **`remove_spaces(text)`**: Removes all spaces from the input string `text`.

44. **`calculate_square_root(number)`**: Approximates the square root of `number` using the Newton-Raphson method.

### File Handling and System Functions:
45. **`find_files_by_extension(directory, extension)`**: Returns a list of files in the directory that have the specified file extension.

46. **`get_curr_dir()`**: Returns the current working directory.

47. **`check_if_file_exists(file_path)`**: Checks if a file exists at `file_path`.

48. **`monitor_new_files(directory, callback)`**: Continuously monitors the directory for new files and calls `callback` whenever new files are added.

49. **`get_system_uptime()`**: Returns the system's uptime in seconds.

50. **`get_cpu_templinux()`**: Retrieves the CPU temperature on a Linux system.

51. **`monitor_file_changes(file_path, callback)`**: Monitors the file for changes and calls `callback` when the file is modified.

52. **`write_to_file(filename, content)`**: Writes the `content` to the specified `filename`.

53. **`read_from_file(filename)`**: Reads and returns the content of the file specified by `filename`.

54. **`parse_json(json_string)`**: Parses a JSON string and returns the corresponding Python object.

55. **`create_file_if_not_exists(filename)`**: Creates a file if it doesn't already exist.

56. **`create_directory(directory)`**: Creates the specified directory if it doesn't exist.

57. **`get_cpu_usage()`**: Returns the current CPU usage percentage using `psutil`.

58. **`get_memory_usage()`**: Returns the current memory usage percentage using `psutil`.

59. **`create_zip_file(source_dir, output_zip)`**: Creates a ZIP archive of the specified `source_dir`.

60. **`extract_zip_file(zip_file, extract_dir)`**: Extracts a ZIP archive to the specified `extract_dir`.

61. **`move_file(source, destination)`**: Moves a file from `source` to `destination`.

62. **`copy_file(source, destination)`**: Copies a file from `source` to `destination`.

63. **`show_file_properties(file_path)`**: Displays properties of a file (size and last modified time).

### HTTP Server Functions:
64. **`start_http_server(ip="0.0.0.0", port=8000)`**: Starts a simple HTTP server on the given `ip` and `port`.

65. **`stop_http_server()`**: Stops the running HTTP server.

66. **`get_server_status(url="http://localhost:8000")`**: Checks if the server at the given URL is up and running.

67. **`set_server_timeout(timeout=10)`**: Sets the timeout for server connections.

68. **`upload_file_to_server(file_path, url="http://localhost:8000/upload")`**: Uploads a file to a server at the specified URL.

69. **`download_file_from_server(file_url, save_path)`**: Downloads a file from the server and saves it to `save_path`.

70. **`CustomRequestHandler`**: A custom request handler for the HTTP server that responds to specific paths ("/" and "/status").

71. **`start_custom_http_server(ip="0.0.0.0", port=8000)`**: Starts a custom HTTP server using the `CustomRequestHandler`.

72. **`set_server_access_logs(log_file="server_access.log")`**: Configures logging to store server access logs.

73. **`get_server_logs(log_file="server_access.log")`**: Retrieves and prints the server access logs.

74. **`restart_http_server()`**: Restarts the HTTP server.

75. **`check_internet_connection()`**: Checks if the system has internet connectivity by pinging `google.com`.

76. **`create_web_server(directory, port=8000)`**: Serves the contents of a directory over HTTP on the specified port.

77. **`create_custom_web_server(html, port=8000)`**: Serves custom HTML content over HTTP on the specified port.

78. **`JynParser(rep)`**: Executes a Python script passed as `rep` in a new context (using `exec()`).

79. **`contains(input_list, substring)`**: Checks if the given `substring` exists within any element of `input_list`.  

80. **`Jusbcam(Device_Name)`**: Scans connected USB devices and checks if `Device_Name` is present in the list of detected devices.

81. **`claw()`**: Claw allows you to create a custom HTTP server with extensive control over its settings. Here are the things you can customize:
    HTML Code – Modify the webpage content as needed.
    IP Address – Choose which IP the server runs on.
    Port – Set the specific port for the server.
    Subdomains – Configure custom subdomains.
    Return Server Logs – Enable or disable server log reporting.

82. **`ConsoleCam()`**: ConsoleCam lets u record and return the new changes in console in a spesific part.

83. **`prn()`**: Prn lets u type faster and basically it just prints same as the print function.