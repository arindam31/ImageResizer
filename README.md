Name: Bulk Image resizer


What works:

1) Images get converted successfully


What next (5th Nov 2015):

Resizer:

1) Percentage can be provided as an input
2) Ratio can be locked or unlocked
3) Choice of extension can be provided
4) Choice of suffix or prefix can be provided
5) Single file choice can be provided - Done
6) Resizing by DPI (Resolution stays the same..DPI changes)

UI:

Done:
1) Add pull down for percentage/ratio - Done
2) Add checkbox to keep proportion - Done
5) suffix/prefix pull down
6) Display extension and size of each file - Done
7) Double clicking should open file with default software
8) Add Convert Button and attach to "resizer" - Done
9) Display size of new created file - Done
10) Popup for no option to convert and integer only - Done
11) Show resolution - Done
12) Add tool tip for everything
13) Add checkbox before each file. - Done
14) Display Estimated size after conversion - DOne
15) Disable editing of cell - Done
16) Add pull down for extension choice - BMP - Done (now ext of each file is detected and used)
17) Add quality options in UI (default can be kept as 80) - DONE
18) Single File image preview - DONE
19) Add a pop up for finished conversion..no of files converted - DONE

Pending:

Add menu bar - Add file, Add folder, Help , About, Reset App
Double clicking table row should open image
Double clicking the single image should open the image in the default image viewer
Check ALL, Un check ALL buttons to be provided
Set limits for text box values

Defects:
1. Selection of a folder with other contents ...app detects other files too - FIXED
2. If 100% selected..file size still changes...band width was 1024 by default... - FIXED
3. Clearing the list does not remove rows...Numbering still present..clicking is possible. - FIXED
4. Double clicking enables text editing the boxes. - FIXED
5. Percentage doesnt reduce exactly when image is JPEG - Now image reduced by size of file - FIXED
6. Choose file , then folder...pics don't show - FIXED
7. If empty folder selected...does not return error - FIXED - (Showing pop up)
8. Single file conversion not working...make diff convert branch for each scenario - FIXED
9. Image resizing formula works fine for bmp..but for other formats do not work so well
10: Pressing escape after pressing "select directory" button crashes the app.