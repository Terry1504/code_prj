
def check_file(file_name):
    print("File ", file_name)
    file_code = open(file_name)
    codes = file_code.readlines()
    file_code.close()

    i = 0
    while (i < len(codes)):
        # Find a message print call
        #     CI_LOG_MSG(CI_ERROR, CI_ERR_INTERNAL_ERR, CI_INTL_ERR_INVALID_OBJ, errmsg);
        #     SPQ_LOG_MSG(CI_ERROR, SPQ_ERR_INTERNAL_ERR, CI_INTL_ERR_PTHREAD_ROUTINE_FAIL, errmsg);
        if (("CI_LOG_MSG" in codes[i]) or ("SPQ_LOG_MSG" in codes[i])):
            call_line = codes[i]

            # In case it's called with multiple line, put them together
            if (";" not in call_line):
                i = i + 1
                next_line = codes[i]
                while (";" not in next_line):
                    call_line = call_line + next_line
                    i = i + 1
                    next_line = codes[i]
                call_line = call_line + next_line

            # Get message macro name
            params = call_line.split(",")
            msg_name = params[1]
            msg_name = msg_name.strip()

            # special treat for those without parameter, e.g: CI_LOG_MSG(CI_ERROR, CI_ERR_CLOSING_CI);
            if msg_name.endswith(");"):
                msg_name = msg_name[:-2]

            # then get the format string from ci locale file
            #     0 = CI_ERR_ACK_THREAD_EXIT, "ACK thread of Stream '%s' will exit due to heartbeat failure(runflag = %d, mstats = %d)."
            #     14 = CI_ERR_CLOSING_CI, "Closing CI."
            #     57 = SPQ_ERR_REWIND_LOG_FILE_FAIL, "Failed to partially rewind the SPQ log file '%s'."
            #     59 = SPQ_ERR_REWIND_LOG_FILE, "The SPQ log file '%s' rewound at index %llu (OQID = 0x%s, Confirmed OQID = 0x%s)."
            j = 0
            msg_name = msg_name + ","
            while (j < len(ci_messages)):
                if (msg_name in ci_messages[j]):
                    break
                j = j + 1
            if (j == len(ci_messages)):
                print("line# ", i+1, " something might be wrong, did not find ", "\n", call_line.strip(), "\n", msg_name)
                continue

            # Now check whether parameter number is same as format string required
            msg_string = ci_messages[j]
            pos = msg_string.find(",")
            format_string = msg_string[pos+1:]
            format_placeholder_number = format_string.count("%")
            if ((len(params) - 2) != format_placeholder_number):
                print("line# ", i+1, " something might be wrong, parameter number did not match ", "\n", call_line.strip(), "\n", msg_string)
            else:
                # print("line# ", i+1, " match", "\n", "\n", call_line.strip(), msg_string)
                pass
        i = i + 1

    print("done ", file_name, "\n")

from datetime import datetime
print("======== START ======== ", datetime.today())

file_ci = open("view/ci.loc")
ci_messages = file_ci.readlines()
file_ci.close()

import glob
file_names = glob.glob("view/*.c")

for current_file in file_names:
    check_file(current_file)

print("======== END ======== ", datetime.today())
