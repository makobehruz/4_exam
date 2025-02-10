function showTab(tab) {
    const tabs = ['schedule', 'students', 'performance'];

    tabs.forEach(t => {
        document.getElementById(`content-${t}`).classList.add('hidden');
        document.getElementById(`tab-${t}`).classList.remove('text-blue-600', 'border-blue-600');
        document.getElementById(`tab-${t}`).classList.add('text-gray-500', 'border-transparent');
    });

    document.getElementById(`content-${tab}`).classList.remove('hidden');
    document.getElementById(`tab-${tab}`).classList.add('text-blue-600', 'border-blue-600');
    document.getElementById(`tab-${tab}`).classList.remove('text-gray-500', 'border-transparent');
}