<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $url = $_POST['url'];
    $ips = [
        "77.92.138.121", "212.102.38.46", "212.102.38.47",
        "77.92.138.126", "77.92.138.120", "89.187.169.43"
    ];

    $results = [];
    foreach ($ips as $ip) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 5);
        $response = curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        if ($response === false) {
            $results[] = ["ip" => $ip, "status_code" => "Error"];
        } else {
            $results[] = ["ip" => $ip, "status_code" => $http_code];
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Test Aracı</title>
</head>
<body>
    <h1>IP Test Aracı</h1>
    <form method="POST">
        <label for="url">Test Edilecek URL:</label>
        <input type="text" id="url" name="url" required>
        <button type="submit">Test Et</button>
    </form>

    <?php if (!empty($results)) : ?>
        <h2>Sonuçlar</h2>
        <table border="1">
            <tr>
                <th>IP Address</th>
                <th>Status Code</th>
            </tr>
            <?php foreach ($results as $result) : ?>
                <tr>
                    <td><?= $result['ip'] ?></td>
                    <td><?= $result['status_code'] ?></td>
                </tr>
            <?php endforeach; ?>
        </table>
    <?php endif; ?>
</body>
</html>
