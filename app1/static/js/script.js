const districts = {
    hn: ["Ba Đình", "Hoàn Kiếm", "Tây Hồ", "Cầu Giấy", "Đống Đa", "Hai Bà Trưng", "Hoàng Mai", "Long Biên", "Nam Từ Liêm", "Bắc Từ Liêm", "Thanh Xuân", "Hà Đông", "Sơn Tây", "Ba Vì", "Chương Mỹ", "Đan Phượng", "Đông Anh", "Gia Lâm", "Hoài Đức", "Mê Linh", "Mỹ Đức", "Phú Xuyên", "Phúc Thọ", "Quốc Oai", "Sóc Sơn", "Thạch Thất", "Thanh Oai", "Thanh Trì", "Thường Tín", "Ứng Hòa"],
    hcm: ["Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Bình Tân", "Bình Thạnh", "Gò Vấp", "Phú Nhuận", "Tân Bình", "Tân Phú", "Thủ Đức"]
    // Thêm các quận huyện khác vào đây nếu cần
};

const provinceSelect = document.getElementById("province");
const districtSelect = document.getElementById("district");

provinceSelect.addEventListener("change", function () {
    const selectedProvince = provinceSelect.value;
    districtSelect.innerHTML = '<option value="">Chọn quận/huyện</option>';

    if (selectedProvince in districts) {
        const districtArray = districts[selectedProvince];
        districtArray.forEach(function (district) {
            const option = document.createElement("option");
            option.text = district;
            option.value = district;
            districtSelect.appendChild(option);
        });
    }
});



// ....
document.getElementById('open-form-btn').addEventListener('click', function () {
    // Hiển thị form popup khi nút được bấm
    document.getElementById('form-popup').style.opacity = '1';
    document.getElementById('form-popup').style.visibility = 'visible';
    document.querySelector('.overlay').style.display = 'block';
});

document.getElementById('close-btn').addEventListener('click', function () {
    // Đóng form popup và overlay khi nút tắt được bấm
    document.getElementById('form-popup').style.opacity = '0';
    document.getElementById('form-popup').style.visibility = 'hidden';
    document.querySelector('.overlay').style.display = 'none';
});

document.getElementById('registration-form').addEventListener('submit', function (event) {
    // Xử lý logic gửi form ở đây (có thể gửi thông tin bằng AJAX hoặc chuyển đến một trang khác)
    alert('Đã gửi thông tin: Tên - ' + document.getElementById('name').value + ', Email - ' + document.getElementById('email').value);
    // Ngăn chặn form gửi đi và làm tải lại trang
    event.preventDefault();
    // Đóng form popup và overlay
    document.getElementById('form-popup').style.opacity = '0';
    document.getElementById('form-popup').style.visibility = 'hidden';
    document.querySelector('.overlay').style.display = 'none';
});