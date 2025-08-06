
import { registry } from "@web/core/registry";

// In this test we will try to fill the contact us form,
// submit it and check if we are redirected to the success page.

registry.category("web_tour.tours").add("my_tour", {
    url: '/contactus',
    steps: () => [
        // Let's fill the form
    ]
});
