/* global gettext */

// Prevent a situation when the translation is not implemented.
if (typeof gettext !== "function") {
    window.gettext = text => text
}

function populate(text, obj) {
    // Map values to the text. E.g. "Text %(value)s."
    for (const [key, value] of Object.entries(obj)) {
        const pattern = new RegExp(`%\\(${key}\\)s`, 'g')
        text = text.replace(pattern, value)
    }
    return text
}


export function handleFormRequiredCheckbox(event) {
    // The event.target is a checkbox - this is the result of selector: .form-required input[type=checkbox]
    const form = event.target.closest("form")
    if (form) {
        // Remove error messages if there are any.
        for (const element of form.querySelectorAll(".aldryn-forms-required-msg, .aldryn-forms-submit-msg")) {
            element.parentNode.removeChild(element)
        }
        // Enable submit button.
        for (const button of form.querySelectorAll('[type=submit]')) {
            button.disabled = false
            button.readOnly = false
        }
    }
}

export function disableButtonSubmit(event, display_message) {
    // Disable button submit to prevent user click more than once.
    event.target.blur()
    for (const button of event.target.querySelectorAll('[type=submit]')) {
        button.disabled = true
        button.readOnly = true
        if (display_message) {
            button.insertAdjacentHTML(
                'afterend',
                '<div class="text-danger aldryn-forms aldryn-forms-submit-msg">'
                + gettext("Please wait. Submitting form...")
                + '</div>')
        }
    }
}

export function handleRequiredFields(event) {
    // Handle required fields.
    let requiredFieldsFulfilled = true
    for (const checkboxset of this.getElementsByClassName("form-required")) {
        const chosen = checkboxset.querySelectorAll("input[type=checkbox]:checked").length
        if (chosen < parseInt(checkboxset.dataset.required_min)) {
            requiredFieldsFulfilled = false
            checkboxset.insertAdjacentHTML(
                'afterend',
                '<div class="text-danger aldryn-forms aldryn-forms-required-msg">'
                + populate(gettext("You have to choose at least %(value)s options (chosen %(chosen)s)."), {
                    value: checkboxset.dataset.required_min, chosen: chosen})
                + '</div>')
        }
    }
    // Do not submit the form if any required fields are missing.
    if (requiredFieldsFulfilled) {
        // Display a message to inform the user that the form has been submitted.
        for (const button of this.querySelectorAll('[type=submit]')) {
            button.insertAdjacentHTML(
                'afterend',
                '<div class="text-danger aldryn-forms aldryn-forms-submit-msg">'
                + gettext("Please wait. Submitting form...")
                + '</div>')
        }
    } else {
        // Some required value is not set.
        event.preventDefault()
        for (const button of this.querySelectorAll('[type=submit]')) {
            button.insertAdjacentHTML(
                'afterend', '<div class="text-danger aldryn-forms aldryn-forms-submit-msg">'
                + gettext("Correct the errors first, please.") + '</div>')
        }
    }
}


function blockSubmit(nodeInput) {
    const form = nodeInput.closest("form")
    for (const button of form.querySelectorAll('[type=submit]')) {
        button.disabled = true
        button.insertAdjacentHTML(
            'afterend', '<div class="text-danger aldryn-forms aldryn-forms-submit-msg">'
            + gettext("Correct the errors first, please.") + '</div>')
    }
}


function unblockSubmit(nodeInput) {
    const form = nodeInput.closest("form")
    for (const button of form.querySelectorAll('[type=submit]')) {
        button.disabled = false
    }
    for (const element of form.getElementsByClassName('aldryn-forms-submit-msg')) {
        element.remove()
    }
}


function handleChangeFilesList(nodeInputFile) {
    const listFileNames = nodeInputFile.parentNode.querySelector('ul.upload-file-names')
    if (listFileNames === null) {
        return
    }
    listFileNames.innerHTML = ''
    unblockSubmit(nodeInputFile)

    const accept = nodeInputFile.accept.length ? nodeInputFile.accept.split(',') : []
    const extensions = [],
        mimetypes = [],
        maim_mimes = []
    let is_valid = true

    let files_size_summary = null
    if (nodeInputFile.dataset.max_size !== null) {
        files_size_summary = 0
        for (let i = 0; i < nodeInputFile.files.length; i++) {
            files_size_summary += nodeInputFile.files[i].size
        }
    }
    if (nodeInputFile.dataset.max_size !== null && files_size_summary > nodeInputFile.dataset.max_size) {
        is_valid = false
        const msg = document.createElement("li")
        msg.classList.add("text-danger")
        msg.appendChild(document.createTextNode(gettext('The total file size has exceeded the specified limit.')))
        listFileNames.appendChild(msg)
    }

    if (nodeInputFile.accept.length) {
        for (let i = 0; i < accept.length; i++) {
            if (accept[i][0] === '.') {
                extensions.push(accept[i])
            } else {
                const mtypes = accept[i].split('/')
                if (mtypes[1] === '*') {
                    maim_mimes.push(mtypes[0])
                } else {
                    mimetypes.push(accept[i])
                }
            }
        }
    }

    for (let i = 0; i < nodeInputFile.files.length; i++) {
        const item = document.createElement("li")
        const file_name = nodeInputFile.files[i].name
        const name = document.createElement("span")
        name.appendChild(document.createTextNode(file_name + " "))
        item.appendChild(name)
        const errors = []
        if (i >= nodeInputFile.dataset.max_files) {
            errors.push(gettext('This file exceeds the uploaded files limit.'))
        }

        let is_expected_type = accept.length ? false : true

        if (!is_expected_type && extensions) {
            const ext = file_name.toLowerCase().match(/\.\w+$/)
            if (ext !== null && extensions.includes(ext[0])) {
                is_expected_type = true
            }
        }
        if (!is_expected_type && mimetypes) {
            if (mimetypes.includes(nodeInputFile.files[i].type)) {
                is_expected_type = true
            }
        }
        if (!is_expected_type && maim_mimes) {
            const mt = nodeInputFile.files[i].type.split('/')
            if (maim_mimes.includes(mt[0])) {
                is_expected_type = true
            }
        }

        if (!is_expected_type) {
            errors.push(gettext('The file type is not among the accpeted types.'))
        }

        if (errors.length) {
            is_valid = false
            name.title = errors.join(" ")
            name.classList.add("fail-upload")
            const icon = document.createElement("img")
            icon.src = '/static/admin/img/icon-alert.svg'
            icon.width = 16
            icon.height = 16
            name.insertBefore(icon, name.firstChild)
        }
        listFileNames.appendChild(item)
    }

    if (!is_valid) {
        blockSubmit(nodeInputFile)
    }
}


export function enableFieldUploadDragAndDrop() {
    for (const input of document.querySelectorAll('input[type=file]')) {
        if (input.dataset.enable_js !== undefined) {
            // <div class="upload-file-frame">
            const uploadFileFrame = document.createElement("div")
            uploadFileFrame.classList.add("upload-file-frame")
            input.parentNode.insertBefore(uploadFileFrame, input)
            input.parentElement.removeChild(input)
            uploadFileFrame.appendChild(input)
            // <ul class="upload-file-names"></ul>
            const listFileNames = document.createElement("ul")
            listFileNames.classList.add("upload-file-names")
            uploadFileFrame.appendChild(listFileNames)
            input.addEventListener('change', (event) => handleChangeFilesList(event.target), false)
            handleChangeFilesList(input)
        }
    }
}
