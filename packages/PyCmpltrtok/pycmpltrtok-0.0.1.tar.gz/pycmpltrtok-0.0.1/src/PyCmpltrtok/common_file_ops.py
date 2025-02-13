import os
import stat
from PyCmpltrtok.common import sep

def get_file_mode(filepath):
    """Gets the file mode of a file and returns it in octal format."""
    try:
        st = os.stat(filepath)
        mode = st.st_mode
        octal_mode = oct(mode)  # Convert to octal representation
        return octal_mode
    except FileNotFoundError:
        return "File not found"
    except Exception as e:  # Catch other potential errors
        return f"An error occurred: {e}"


def interpret_file_mode(octal_mode):
    """Interprets the octal file mode and returns a human-readable string."""
    if octal_mode == "File not found" or octal_mode.startswith("An error"):
        return octal_mode  # Return the error message as is

    mode_str = ""
    # Check file type
    if stat.S_ISDIR(int(octal_mode, 8)):  # Convert from octal to int
        mode_str += "d"
    elif stat.S_ISLNK(int(octal_mode, 8)):
        mode_str += "l"
    else:
        mode_str += "-"

    # Check permissions for owner, group, and others
    for i in range(3):  # Iterate through owner, group, others
        for j in range(3):  # Iterate through r, w, x
            bit = (int(octal_mode, 8) >> (8 - (i * 3 + j))) & 1
            if bit:
                if j == 0:
                    mode_str += "r"
                elif j == 1:
                    mode_str += "w"
                elif j == 2:
                    mode_str += "x"
            else:
                mode_str += "-"
    return mode_str


def change_file_mode(filepath, new_mode_octal):
    """Changes the file mode of a file.

    Args:
        filepath: The path to the file.
        new_mode_octal: The new file mode in octal string format (e.g., "0o755").
    """
    try:
        # Convert octal string to integer
        new_mode_int = int(new_mode_octal, 8)

        os.chmod(filepath, new_mode_int)
        print(f"Mode of '{filepath}' changed to {new_mode_octal}")
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except OSError as e:  # Catch potential permission errors or other OS errors
        print(f"Error changing mode: {e}")
    except ValueError:
        print("Invalid octal mode. Please provide a valid octal string (e.g., '0o755').")


if '__main__' == __name__:
    
    def main():
        sep('Start')
        # Example usage:
        filepath = "/home/yunpeng/.data/PyCmpltrtok/auth/mongo/mongodb.tpl.yaml"  # Replace with your file's path
        print('filepath:', filepath)
        
        def check(filepath):
            sep('check')
            octal_mode = get_file_mode(filepath)
            print('octal_mode:', octal_mode)

            if not octal_mode.startswith("An error") and octal_mode != "File not found":
                human_readable_mode = interpret_file_mode(octal_mode)
                print(f"Octal Mode: {octal_mode}")
                print(f"Human-Readable Mode: {human_readable_mode}")
            else:
                print(octal_mode) # Print the error message

        check(filepath)

        sep('Change mode')
        # Example 3: (More restrictive) Read/write only by owner
        new_mode = "0o600"  # rw-------
        change_file_mode(filepath, new_mode)

        check(filepath)
    
    main()
    sep('All over')
    