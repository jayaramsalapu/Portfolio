document.addEventListener('DOMContentLoaded', function() {
    function initCKEditor() {
        const textareas = document.querySelectorAll('textarea.ckeditor-5');
        textareas.forEach(textarea => {
            if (textarea.dataset.ckeditorInitialized) return;
            textarea.dataset.ckeditorInitialized = 'true';
            
            ClassicEditor
                .create(textarea, {
                    toolbar: [
                        'heading', '|',
                        'bold', 'italic', 'link', '|',
                        'bulletedList', 'numberedList', '|',
                        'insertTable', 'codeBlock', 'blockQuote', '|',
                        'undo', 'redo'
                    ],
                    heading: {
                        options: [
                            { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
                            { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
                            { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },
                            { model: 'heading3', view: 'h3', title: 'Heading 3', class: 'ck-heading_heading3' }
                        ]
                    }
                })
                .then(editor => {
                    // Update original textarea when editor content changes
                    editor.model.document.on('change:data', () => {
                        textarea.value = editor.getData();
                    });
                    
                    // Keep textarea in sync before any form submission
                    const form = textarea.closest('form');
                    if (form) {
                        form.addEventListener('submit', () => {
                            textarea.value = editor.getData();
                        });
                    }
                })
                .catch(error => {
                    console.error('Error initializing CKEditor 5:', error);
                });
        });
    }

    // Run on initial page load
    initCKEditor();
    
    // Support Django admin dynamic formsets (e.g. adding inline elements dynamically)
    if (window.django && window.django.jQuery) {
        window.django.jQuery(document).on('formset:added', function(event, $row, formsetName) {
            initCKEditor();
        });
    }
});
