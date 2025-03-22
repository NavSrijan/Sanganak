
.org 0x000
ADD 0x010    # Add value at 0x100 to AC
AND @0x011   # AND value at effective address (from 0x101) with AC
CLA          # Clear AC
OUT          # Output AC to OUTR

.org 0x010
.data 0x0005 # Data for ADD
.data 0x00FF # Data for AND (effective address at 0x101)

