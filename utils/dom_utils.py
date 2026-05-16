class DOMUtils:

    @staticmethod
    def get_interactable_elements(driver):

        script = """
        const elements = Array.from(document.querySelectorAll(
            'button, input, textarea, select, a, [role="button"], [contenteditable="true"]'
        ));

        return elements.map((el, index) => {
            return {
                index: index,
                tag: el.tagName.toLowerCase(),
                text: (el.innerText || el.value || '').trim(),
                type: el.getAttribute('type') || '',
                id: el.id || '',
                name: el.getAttribute('name') || '',
                className: el.className || '',
                placeholder: el.getAttribute('placeholder') || '',
                ariaLabel: el.getAttribute('aria-label') || '',
                dataTestId: el.getAttribute('data-testid') || '',
                href: el.getAttribute('href') || '',
                visible: !!(
                    el.offsetWidth ||
                    el.offsetHeight ||
                    el.getClientRects().length
                )
            };
        }).filter(el => el.visible);
        """

        return driver.execute_script(script)