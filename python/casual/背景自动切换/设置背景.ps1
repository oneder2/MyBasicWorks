# 设置文件夹路径
${folderPath} = "D:\鼓捣Python\Backgroundautomaticsetting\auto\set"
 
 
# 获取文件夹中所有图片的路径
$images = Get-ChildItem -Path $folderPath -Filter *.jpg | Sort-Object {Get-Random}
# 初始化计数器
$wallpaperChangeCount = 0
# 设置更换壁纸的间隔时间（秒）
$intervalInSeconds = 120  #  更换壁纸,60*n，即120为2分钟
 
# 加载 User32.dll
Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class User32 {
        [DllImport("user32.dll", SetLastError = true)]
        public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
    }
"@
 
# 无限循环，定时更换壁纸
while ($true) {
    foreach ($image in $images) {
        # 设置壁纸
        [User32]::SystemParametersInfo(20, 0, $image.FullName, 3)
       # 增加计数器
        $wallpaperChangeCount++
 
        # 显示切换信息
        Write-Host " 本次脚本运行切换了 $wallpaperChangeCount  张壁纸"
        Write-Host "当前壁纸名为  $image "
        # 等待一定时间
        Start-Sleep -Seconds $intervalInSeconds
    }
}
 