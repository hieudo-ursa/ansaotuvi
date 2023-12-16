# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from ansaotuvi.AmDuong import nguHanh


class Sao(object):
    """Summary
        Args:
            saoID (int): 1, 2, ...
            saoTen (TYPE): Tử vi, Tham lang,...
            saoNguHanh (TYPE): K, M, T, H, O
            saoLoai (str, optional): Sao tốt < 10, sau xấu > 10
                1: Chính tinh, 2: Phụ tinh nói chung
                3: Quý tinh, 4: Quyền tinh, 5: Phúc tinh, 6: Văn tinh
                7: Đài các tinh, 8: Đào hoa tinh

                11: Sát tinh, 12: Bại tinh, 13: Ám tinh, 14: Dâm tinh,
                15: Hình tinh
            saoPhuongVi (str, optional): Bắc Đẩu tinh, Nam Bắc Đẩu tinh
            saoAmDuong (str, optional): Âm Dương của sao
            vongTrangSinh (int, optional): 0/None: Không thuộc vòng Tràng sinh
                                            1: Thuộc vòng Tràng sinh
        """

    def __init__(self, saoID, saoTen, saoNguHanh, saoLoai=2, saoPhuongVi="",
                 saoAmDuong="", vongTrangSinh=0):
        super(Sao, self).__init__()
        self.saoID = saoID
        self.saoTen = saoTen
        self.saoNguHanh = saoNguHanh
        self.saoLoai = saoLoai
        self.saoPhuongVi = saoPhuongVi
        self.saoAmDuong = saoAmDuong
        self.vongTrangSinh = vongTrangSinh
        self.cssSao = nguHanh(saoNguHanh)['css']
        self.saoDacTinh = None

    def anDacTinh(self, dacTinh):
        """An Đặc tính cho sao: V, M, Đ, B, H
        Args: saoDacTinh (str): Đặc tính của sao, Vượng (V), Miếu (M),
                                Đắc (Đ), Bình (B), Hãm (H)
        Returns:
            object: self
        """
        # "V": "vuongDia",
        # "M": "mieuDia",
        # "Đ": "dacDia",
        # "B": "binhHoa",
        # "H": "hamDia",
        self.saoDacTinh = dacTinh
        # self.saoTen += " (%s)" % dacTinh
        # self.cssSao = dt[dacTinh]
        return self

    def anCung(self, saoViTriCung):
        """Summary

        Returns:
            TYPE: Description
        """
        self.saoViTriCung = saoViTriCung
        return self


# Tử vi tinh hệ
saoTuVi = Sao(1, u"Tử vi", "O", 1, u"Đế tinh", -1, 0)
saoLiemTrinh = Sao(2, u"Liêm trinh", "H", 1, u"Bắc đẩu tinh", -1, 0)
saoThienDong = Sao(3, u"Thiên đồng", "T", 1, u"Bắc đẩu tinh", 1, 0)
saoVuKhuc = Sao(4, u"Vũ khúc", "K", 1, u"Bắc đẩu tinh", -1, 0)
saoThaiDuong = Sao(5, u"Thái Dương", "H", 1, u"Nam đẩu tinh", 1, 0)
saoThienCo = Sao(6, u"Thiên cơ", "M", 1, u"Nam đẩu tinh", -1, 0)

# Thiên phủ tinh hệ
saoThienPhu = Sao(7, u"Thiên phủ", "O", 1, u"Nam đẩu tinh", 1, 0)
saoThaiAm = Sao(8, u"Thái âm", "T", 1, u"Bắc đẩu tinh", -1, 0)
saoThamLang = Sao(9, u"Tham lang", "T", 1, u"Bắc đẩu tinh", 1, 0)
saoCuMon = Sao(10, u"Cự môn", "T", 1, u"Bắc đẩu tinh", -1, 0)
saoThienTuong = Sao(11, u"Thiên tướng", "T", 1, u"Nam đẩu tinh", 1, 0)
saoThienLuong = Sao(12, u"Thiên lương", "O", 1, u"Nam đẩu tinh", 1, 0)
saoThatSat = Sao(13, u"Thất sát", "K", 1, u"Nam đẩu tinh", 1, 0)
saoPhaQuan = Sao(14, u"Phá quân", "T", 1, u"Bắc đẩu tinh", -1, 0)

# Vòng Địa chi - Thái tuế
saoThaiTue = Sao(15, u"Thái tuế", "H", 15, "", 0)
saoThieuDuong = Sao(16, u"Thiếu dương", "H", 5)
saoTangMon = Sao(17, u"Tang môn", "M", 12)
saoThieuAm = Sao(18, u"Thiếu âm", "T", 5)
saoQuanPhu3 = Sao(19, u"Quan phù", "H", 12)
saoTuPhu = Sao(20, u"Tử phù", "K", 12)
saoTuePha = Sao(21, u"Tuế phá", "H", 12)
saoLongDuc = Sao(22, u"Long đức", "T", 5)
saoBachHo = Sao(23, u"Bạch hổ", "K", 12)
saoPhucDuc = Sao(24, u"Phúc đức", "O", 5)
saoDieuKhach = Sao(25, u"Điếu khách", "H", 12)
saoTrucPhu = Sao(26, u"Trực phù", "K", 16)

#  Vòng Thiên can - Lộc tồn
saoLocTon = Sao(27, u"Lộc tồn", "O", 3, saoAmDuong=-1)
saoBacSy = Sao(109, u"Bác sỹ", "T", 5, )
saoLucSi = Sao(28, u"Lực sĩ", "H", 2)
saoThanhLong = Sao(29, u"Thanh long", "T", 5)
saoTieuHao = Sao(30, u"Tiểu hao", "H", 12)
saoTuongQuan = Sao(31, u"Tướng quân", "M", 4)
saoTauThu = Sao(32, u"Tấu thư", "K", 3)
saoPhiLiem = Sao(33, u"Phi liêm", "H", 2)
saoHyThan = Sao(34, u"Hỷ thần", "H", 5)
saoBenhPhu = Sao(35, u"Bệnh phù", "O", 12)
saoDaiHao = Sao(36, u"Đại hao", "H", 12)
saoPhucBinh = Sao(37, u"Phục binh", "H", 13)
saoQuanPhu2 = Sao(38, u"Quan phù", "H", 12)

# Vòng Tràng sinh
saoTrangSinh = Sao(39, u"Tràng sinh", "T", 5, vongTrangSinh=1)
saoMocDuc = Sao(40, u"Mộc dục", "T", 14, vongTrangSinh=1)
saoQuanDoi = Sao(41, u"Quan đới", "K", 4, vongTrangSinh=1)
saoLamQuan = Sao(42, u"Lâm quan", "K", 7, vongTrangSinh=1)
saoDeVuong = Sao(43, u"Đế vượng", "K", 5, vongTrangSinh=1)
saoSuy = Sao(44, u"Suy", "T", 12, vongTrangSinh=1)
saoBenh = Sao(45, u"Bệnh", "H", 12, vongTrangSinh=1)
saoTu = Sao(46, u"Tử", "H", 12, vongTrangSinh=1)
saoMo = Sao(47, u"Mộ", "O", vongTrangSinh=1)
saoTuyet = Sao(48, u"Tuyệt", "O", 12, vongTrangSinh=1)
saoThai = Sao(49, u"Thai", "O", 14, vongTrangSinh=1)
saoDuong = Sao(50, u"Dưỡng", "M", 2, vongTrangSinh=1)

# Lục sát
#    Kình dương đà la
saoDaLa = Sao(51, u"Đà la", "K", 11, saoAmDuong=-1)
saoKinhDuong = Sao(52, u"Kình dương", "K", 11, saoAmDuong=1)

#    Địa không - Địa kiếp
saoDiaKhong = Sao(53, u"Địa không", "H", 11, saoAmDuong=1)
saoDiaKiep = Sao(54, u"Địa kiếp", "H", 11, saoAmDuong=-1)

#    Hỏa tinh - Linh tinh
saoLinhTinh = Sao(55, u"Linh tinh", "H", 11, saoAmDuong=-1)
saoHoaTinh = Sao(56, u"Hỏa tinh", "H", 11, saoAmDuong=1)

# Sao Âm Dương
#    Văn xương - Văn khúc
saoVanXuong = Sao(57, u"Văn xương", "K", 6, saoAmDuong=1)
saoVanKhuc = Sao(58, u"Văn Khúc", "T", 6, saoAmDuong=-1)

#    Thiên khôi - Thiên Việt
saoThienKhoi = Sao(59, u"Thiên khôi", "H", 6, saoAmDuong=1)
saoThienViet = Sao(60, u"Thiên việt", "H", 6, saoAmDuong=-1)

#    Tả phù - Hữu bật
saoTaPhu = Sao(61, u"Tả phù", "O", 2, saoAmDuong=1)
saoHuuBat = Sao(62, u"Hữu bật", "T", 2, saoAmDuong=-1)

#    Long trì - Phượng các
saoLongTri = Sao(63, u"Long trì", "T", 3, saoAmDuong=1)
saoPhuongCac = Sao(64, u"Phượng các", "O", 3, saoAmDuong=1)

#    Tam thai - Bát tọa
saoTamThai = Sao(65, u"Tam thai", "O", 7, saoAmDuong=1)
saoBatToa = Sao(66, u"Bát tọa", "O", 7, saoAmDuong=-1)

#    Ân quang - Thiên quý
saoAnQuang = Sao(67, u"Ân quang", "M", 3)
saoThienQuy = Sao(68, u"Thiên quý", "O", 3)

# Sao đôi khác
saoThienKhoc = Sao(69, u"Thiên khốc", "T", 12)
saoThienHu = Sao(70, u"Thiên hư", "T", 12)
saoThienDuc = Sao(71, u"Thiên đức", "H", 5)
saoNguyetDuc = Sao(72, u"Nguyệt đức", "H", 5)
saoThienHinh = Sao(73, u"Thiên hình", "H", 15)
saoThienRieu = Sao(74, u"Thiên riêu", "T", 13)
saoThienY = Sao(75, u"Thiên y", "T", 5)
saoQuocAn = Sao(76, u"Quốc ấn", "O", 6)
saoDuongPhu = Sao(77, u"Đường phù", "M", 4)
saoDaoHoa = Sao(78, u"Đào hoa", "M", 8)
saoHongLoan = Sao(79, u"Hồng loan", "T", 8)
saoThienHy = Sao(80, u"Thiên hỷ", "T", 5)
saoThienGiai = Sao(81, u"Thiên giải", "H", 5)
saoDiaGiai = Sao(82, u"Địa giải", "O", 5)
saoGiaiThan = Sao(83, u"Giải thần", "M", 5)
saoThaiPhu = Sao(84, u"Thai phụ", "O", 6, saoAmDuong=1)
saoPhongCao = Sao(85, u"Phong cáo", "O", 4, saoAmDuong=-1)
saoThienTai = Sao(86, u"Thiên tài", "O", 2)
saoThienTho = Sao(87, u"Thiên thọ", "O", 5)
saoThienThuong = Sao(88, u"Thiên thương", "O", 12)
saoThienSu = Sao(89, u"Thiên sứ", "T", 12)
saoThienLa = Sao(90, u"Thiên la", "O", 12)
saoDiaVong = Sao(91, u"Địa võng", "O", 12)
saoHoaKhoa = Sao(92, u"Hóa khoa", "K", 5)
saoHoaQuyen = Sao(93, u"Hóa quyền", "H", 4)
saoHoaLoc = Sao(94, u"Hóa lộc", "M", 3)
saoHoaKy = Sao(95, u"Hóa kỵ", "T", 13)
saoCoThan = Sao(96, u"Cô thần", "O", 13)
saoQuaTu = Sao(97, u"Quả tú", "O", 13)
saoThienMa = Sao(98, u"Thiên mã", "H", 3)
saoPhaToai = Sao(99, u"Phá toái", "H", 12)
saoThienQuan = Sao(100, u"Thiên quan", "H", 5)
saoThienPhuc = Sao(101, u"Thiên phúc", "H", 5)
saoLuuHa = Sao(102, u"Lưu hà", "T", 12)
saoThienTru = Sao(103, u"Thiên trù", "O", 5)
saoKiepSat = Sao(104, u"Kiếp sát", "H", 11)
saoHoaCai = Sao(105, u"Hoa cái", "K", 14)
saoVanTinh = Sao(106, u"LN. Văn tinh", "H", 6)
saoDauQuan = Sao(107, u"Đẩu quân", "H", 5)
saoThienKhong = Sao(108, u"Thiên không", "H", 11)
