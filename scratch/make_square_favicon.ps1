Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\Loops-IT\.gemini\antigravity-ide\brain\ae48aa8b-c616-4ebc-a58f-41881466da28\media__1783059611563.png"
$destPathPng = "d:\laragon\www\hostinger\public\favicon.png"
$destPathIco = "d:\laragon\www\hostinger\public\favicon.ico"

$destPathCtcPng = "d:\laragon\www\hostinger\public\ctc\favicon.png"
$destPathCtcIco = "d:\laragon\www\hostinger\public\ctc\favicon.ico"

# Load source image
$srcImg = [System.Drawing.Image]::FromFile($srcPath)
$srcW = 228 # Bounding box content width
$srcH = 616 # Bounding box content height

# Let's apply a 1.6x horizontal stretch factor to make the loops wider and readable in the tab
$stretchFactor = 1.6
$drawW = [Math]::Round($srcW * $stretchFactor)
$drawH = $srcH

Write-Output "Source content: $srcW x $srcH"
Write-Output "Stretched content: $drawW x $drawH"

# We want a square canvas matching the height
$squareSize = $srcH

# Create new square bitmap with transparent background
$bmp = New-Object System.Drawing.Bitmap($squareSize, $squareSize)
$graphics = [System.Drawing.Graphics]::FromImage($bmp)

# Set interpolation mode and graphics settings for high quality scaling
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# Clear with transparency
$graphics.Clear([System.Drawing.Color]::Transparent)

# Calculate centering coordinates
$xOffset = [Math]::Floor(($squareSize - $drawW) / 2)
$yOffset = 0

# Draw the source image onto the square canvas with the horizontal stretch
# We crop the source content (0, 0, 228, 616) and draw it stretched to (xOffset, yOffset, drawW, drawH)
$srcRect = New-Object System.Drawing.Rectangle(0, 0, $srcW, $srcH)
$destRect = New-Object System.Drawing.Rectangle($xOffset, $yOffset, $drawW, $drawH)
$graphics.DrawImage($srcImg, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)

# Dispose source image to unlock file
$srcImg.Dispose()
$graphics.Dispose()

# Save as PNG
$bmp.Save($destPathPng, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Save($destPathCtcPng, [System.Drawing.Imaging.ImageFormat]::Png)
Write-Output "Saved stretched square PNGs."

# Save resized 32x32 favicon.ico
$icoSize = 32
$resizedBmp = New-Object System.Drawing.Bitmap($icoSize, $icoSize)
$resizedGraphics = [System.Drawing.Graphics]::FromImage($resizedBmp)
$resizedGraphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$resizedGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$resizedGraphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$resizedGraphics.Clear([System.Drawing.Color]::Transparent)
$resizedGraphics.DrawImage($bmp, 0, 0, $icoSize, $icoSize)
$resizedGraphics.Dispose()

$resizedBmp.Save($destPathIco, [System.Drawing.Imaging.ImageFormat]::Png)
$resizedBmp.Save($destPathCtcIco, [System.Drawing.Imaging.ImageFormat]::Png)
Write-Output "Saved 32x32 stretched favicon.ico."

# Clean up
$resizedBmp.Dispose()
$bmp.Dispose()

Write-Output "All operations completed successfully!"
