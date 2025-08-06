
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("my_tour", {
    url: '/contactus',
    steps: () => [
        {
            content: "Fill 'Name' field",
            trigger: "input[name='name']",
            run: "edit Arib",
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
        {
            content: "Submit the form",
            trigger: "a:contains('Submit')",
            run: "click",
            expectUnloadPage: true,
        },
        {
            content: 'Check form is submitted',
            trigger: '#wrap:has(h1:contains("Thank You!"))',
        },
    ]
});
