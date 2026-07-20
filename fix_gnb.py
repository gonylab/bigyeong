with open('index2.html', 'r') as f:
    c = f.read()

# ============================================================
# 1. 모든 서브페이지 GNB 버튼: X → 햄버거(openMenu)로 통일
# ============================================================

# rlo-gnb: closeAllRoomOverlay → openMenu
c = c.replace(
    '    <button class="gnb-menu" onclick="closeAllRoomOverlay()">\n      <svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>\n    </button>',
    '    <button class="gnb-menu" onclick="openMenu()">\n      <svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>\n    </button>'
)

# splo-gnb: closeAllSpOverlay → openMenu (X 아이콘 → 햄버거)
c = c.replace(
    '    <button class="gnb-menu" onclick="closeAllSpOverlay()">\n      <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>\n    </button>',
    '    <button class="gnb-menu" onclick="openMenu()">\n      <svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>\n    </button>'
)

# resv-guide: closeResvGuide → openMenu (X → 햄버거)
c = c.replace(
    '    <button class="gnb-menu" onclick="closeResvGuide()"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>',
    '    <button class="gnb-menu" onclick="openMenu()"><svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg></button>'
)

# specialOverlay: closeSpecialOverlay → openMenu (X → 햄버거)
c = c.replace(
    '    <button class="gnb-menu" onclick="closeSpecialOverlay()">\n      <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>\n    </button>',
    '    <button class="gnb-menu" onclick="openMenu()">\n      <svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>\n    </button>'
)

# galleryOverlay: closeGalleryOverlay → openMenu (X → 햄버거)
c = c.replace(
    '    <button class="gnb-menu" onclick="closeGalleryOverlay()">\n      <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>\n    </button>',
    '    <button class="gnb-menu" onclick="openMenu()">\n      <svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>\n    </button>'
)

# travelOverlay: closeTravelOverlay → openMenu (X → 햄버거)
c = c.replace(
    '    <button class="gnb-menu" onclick="closeTravelOverlay()">\n      <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>\n    </button>',
    '    <button class="gnb-menu" onclick="openMenu()">\n      <svg viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>\n    </button>'
)

# ============================================================
# 2. 서브페이지 헤더: < 동그라미 버튼 제거 + 디자인 개선
#    slo-header: 기존 back 버튼+타이틀 → 타이틀+서브 세련된 디자인
# ============================================================

# specialOverlay slo-header
c = c.replace(
    '''  <!-- 헤더 -->
  <div class="slo-header">
    <button class="slo-back" onclick="closeSpecialToMenu()">
      <svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
    </button>
    <div>
      <div class="slo-header-title">스페셜</div>
      <div class="slo-header-sub">SPECIAL THINGS</div>
    </div>
  </div>''',
    '''  <!-- 헤더 -->
  <div class="slo-header">
    <div class="slo-header-title">스페셜</div>
    <div class="slo-header-sub">SPECIAL THINGS</div>
  </div>'''
)

# galleryOverlay slo-header
c = c.replace(
    '''  <!-- 헤더 -->
  <div class="slo-header">
    <button class="slo-back" onclick="closeGalleryOverlay()">
      <svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
    </button>
    <div>
      <div class="slo-header-title">갤러리</div>
      <div class="slo-header-sub">GALLERY</div>
    </div>
  </div>''',
    '''  <!-- 헤더 -->
  <div class="slo-header">
    <div class="slo-header-title">갤러리</div>
    <div class="slo-header-sub">GALLERY</div>
  </div>'''
)

# travelOverlay slo-header
c = c.replace(
    '''  <!-- 헤더 -->
  <div class="slo-header">
    <button class="slo-back" onclick="closeTravelOverlay()">
      <svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
    </button>
    <div>
      <div class="slo-header-title">주변여행지</div>
      <div class="slo-header-sub">NEARBY ATTRACTIONS</div>
    </div>
  </div>''',
    '''  <!-- 헤더 -->
  <div class="slo-header">
    <div class="slo-header-title">주변여행지</div>
    <div class="slo-header-sub">NEARBY ATTRACTIONS</div>
  </div>'''
)

# splo-header: < 버튼 제거
c = c.replace(
    '''  <div class="splo-header">
    <button class="splo-back" onclick="backToMenuFromSp()">
      <svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
    </button>
    <div>
      <div class="splo-header-title">스페셜</div>
      <div class="splo-header-sub">SPECIAL THINGS</div>
    </div>
  </div>''',
    '''  <div class="splo-header">
    <div class="splo-header-title">스페셜</div>
    <div class="splo-header-sub">SPECIAL THINGS</div>
  </div>'''
)

# ============================================================
# 3. CSS 개선: slo-header 디자인 세련되게
# ============================================================

old_slo_header_css = '''.slo-header{
  display:flex;align-items:center;gap:12px;
  padding:14px 20px 16px;border-bottom:1px solid rgba(0,0,0,.08);
  background:#f5f1eb;
}
.slo-back{
  width:40px;height:40px;border-radius:50%;background:rgba(0,0,0,.06);
  border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.slo-back svg{width:18px;height:18px;stroke:#1a1a1a;stroke-width:2;fill:none;}
.slo-header-title{
  flex:1;font-size:20px;font-weight:700;color:#1a1a1a;letter-spacing:-.02em;
}
.slo-header-sub{
  font-size:11px;font-weight:400;color:#b4915a;letter-spacing:.06em;margin-top:2px;
}'''

new_slo_header_css = '''.slo-header{
  display:flex;flex-direction:column;gap:2px;
  padding:18px 20px 16px;border-bottom:1px solid rgba(0,0,0,.08);
  background:#f5f1eb;
}
.slo-header-title{
  font-size:22px;font-weight:700;color:#1a1a1a;letter-spacing:-.03em;
}
.slo-header-sub{
  font-size:11px;font-weight:400;color:#b4915a;letter-spacing:.12em;
}'''

c = c.replace(old_slo_header_css, new_slo_header_css)

# splo-header CSS 개선
old_splo_header_css = '''.splo-header{
  display:flex;align-items:center;gap:12px;
  padding:14px 20px 14px;
  border-bottom:1px solid rgba(0,0,0,.07);
  position:sticky;top:56px;background:#f5f1eb;z-index:99;
}
.splo-back{background:none;border:none;padding:4px;cursor:pointer;display:flex;align-items:center;}
.splo-back svg{width:18px;height:18px;stroke:#1a1a1a;stroke-width:2;fill:none;}
.splo-header-title{font-size:15px;font-weight:700;color:#1a1a1a;}
.splo-header-sub{font-size:11px;color:#888;letter-spacing:.08em;}'''

new_splo_header_css = '''.splo-header{
  display:flex;flex-direction:column;gap:2px;
  padding:18px 20px 16px;
  border-bottom:1px solid rgba(0,0,0,.07);
  position:sticky;top:56px;background:#f5f1eb;z-index:99;
}
.splo-header-title{font-size:22px;font-weight:700;color:#1a1a1a;letter-spacing:-.03em;}
.splo-header-sub{font-size:11px;color:#b4915a;letter-spacing:.12em;}'''

c = c.replace(old_splo_header_css, new_splo_header_css)

with open('index2.html', 'w') as f:
    f.write(c)
print('done')
