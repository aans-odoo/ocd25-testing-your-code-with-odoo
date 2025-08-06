
import { registry } from "@web/core/registry";

// In this test we will try to fill the contact us form,
// submit it and check if we are redirected to the success page.

registry.category("web_tour.tours").add("my_tour", {
    url: '/contactus',
    steps: () => [
        // Steps to fill the form
        {
            content: "Fill 'Name' field",
            trigger: "input[name='name']",
            run: "edit Hello", // types "Hello" in our target element
        },
        {
            content: "Fill 'Email' field",
            trigger: "input[name='email_from']",
            run: "edit arib@odoo.com",
        },
        {
            content: "Fill 'Subject' field",
            trigger: "input[name='subject']",
            run: "edit Test subject",
        },
        {
            content: "Fill 'Question' field",
            trigger: "textarea[name='description']",
            run: "edit My test question",
        },

        // Submit form
        {
            content: "Submit the form",
            trigger: "a:contains('Submit')",
            run: "click",
            expectUnloadPage: true,
        },

        // Let's check if we are redirected to the success page
        {
            content: 'Check form is submitted',
            trigger: '#wrap:has(h1:contains("Thank You!"))',
        },
    ]
});
