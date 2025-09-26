/* INIT */
document.addEventListener('DOMContentLoaded', () => {
    const createTaskBtn = document.getElementById('openCreateTaskModal');
    const modal         = document.getElementById('createTaskModal');
    const closeButton   = document.querySelector('.close-button');
    const cancelBtn     = document.getElementById('cancelCreate');
    const promotionForm = document.getElementById('promotionForm');
    const activityTableBody = document.getElementById('activityTableBody');

    /* DATA */
    let promotions = [
        { campaignName: 'Summer Sale',       status: 'active',    startDate: '2024-07-01', endDate: '2024-07-01', engagement: 75 },
        { campaignName: 'Back to School',    status: 'completed', startDate: '2024-08-15', endDate: '2024-08-15', engagement: 90 },
        { campaignName: 'Holiday Promotion', status: 'scheduled', startDate: '2024-12-01', endDate: '2024-12-01', engagement: 0  },
        { campaignName: 'Spring Collection', status: 'draft',     startDate: '2025-03-01', endDate: '2025-03-01', engagement: 0  },
        { campaignName: 'Clearance Event',   status: 'active',    startDate: '2025-04-15', endDate: '2025-04-15', engagement: 60 },
        { campaignName: 'Clearance Event',   status: 'completed', startDate: '2025-04-15', endDate: '2025-04-15', engagement: 0  }
    ];

    /* HELPERS */
    const statusToBadge = s => ({ active:'is-active', completed:'is-completed', scheduled:'is-scheduled', draft:'is-draft' }[s] || 'is-draft');
    const titleCase = s => s.charAt(0).toUpperCase() + s.slice(1);
    const formatDate = ds => new Date(ds).toLocaleDateString('en-GB', { day:'numeric', month:'short', year:'numeric' });

    const openModal  = () => { modal.classList.add('is-open'); document.body.classList.add('body-lock'); };
    const closeModal = () => { modal.classList.remove('is-open'); document.body.classList.remove('body-lock'); promotionForm.reset(); };

    /* RENDER */
    function renderPromotions() {
        activityTableBody.innerHTML = promotions.map(p => `
            <tr>
                <td>${p.campaignName}</td>
                <td><span class="badge ${statusToBadge(p.status)}">${titleCase(p.status)}</span></td>
                <td>${formatDate(p.startDate)}</td>
                <td>${formatDate(p.endDate)}</td>
                <td>
                    <div class="engage">
                        <div class="progress"><div class="progress-bar" style="width:${p.engagement}%"></div></div>
                        <span class="pct">${p.engagement}%</span>
                    </div>
                </td>
            </tr>
        `).join('');
        updateSummary();
    }

    function updateSummary() {
        document.getElementById('totalPromotionCount').textContent  = promotions.length;
        document.getElementById('activePromotionCount').textContent = promotions.filter(p => p.status === 'active').length;
        const total = promotions.reduce((s, p) => s + (Number(p.engagement) || 0), 0);
        const avg   = promotions.length ? (total / promotions.length).toFixed(1) : 0;
        document.getElementById('progressRate').textContent = `${avg}%`;
    }

    /* EVENTS */
    if (createTaskBtn) createTaskBtn.addEventListener('click', openModal);
    if (closeButton)   closeButton.addEventListener('click', closeModal);
    if (cancelBtn)     cancelBtn.addEventListener('click', closeModal);

    window.addEventListener('click', e => { if (e.target === modal) closeModal(); });
    window.addEventListener('keydown', e => { if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal(); });

    promotionForm.addEventListener('submit', e => {
        e.preventDefault();
        const campaignName = document.getElementById('campaignName').value.trim();
        const status       = document.getElementById('status').value;
        const startDate    = document.getElementById('startDate').value;
        const endDate      = document.getElementById('endDate').value;
        const engagement   = Math.max(0, Math.min(100, parseInt(document.getElementById('engagement').value, 10) || 0));

        promotions.push({ campaignName, status, startDate, endDate, engagement });
        renderPromotions();
        closeModal();
    });

    /* INIT */
    renderPromotions();
});
