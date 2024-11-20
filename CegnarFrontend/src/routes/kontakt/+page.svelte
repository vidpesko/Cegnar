<script>
    // API Client
    import { getSpecificProduct } from "$lib/api/client";
    // Components
    import Hero from "$lib/components/Hero.svelte";
    import Toast from "$lib/components/Toast.svelte";
    import NavigationMenu from "$lib/components/NavigationMenu.svelte";
    // Icons
    import PhoneIcon from '~icons/mdi/phone';
    import CustomIcon from '~icons/gridicons/customize';
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import InfoIcon from '~icons/material-symbols/info-outline-rounded';
    import ErrorIcon from '~icons/material-symbols/error-circle-rounded';
    import TrashIcon from '~icons/material-symbols/delete-outline-rounded';
    // Secrets
    import {
        PUBLIC_GOOGLE_MAPS_EMBED_API_KEY
    } from "$env/static/public";
    // Other
    import { page } from '$app/stores';
    import { onMount } from "svelte";

    export let data, form;
    $: pageData = data.contact;
    $: productCategories = data.categories;
    $: settings = data.settings

    let name;
    let email;
    let contactReason = "izdelave po naročilu";
    let message;
    let productId = $page.url.searchParams.get("izdelek") || "";
    let wantedProductPromise;

    // Handle navigation menu
    let menuOpened = false;

    function openNavigationMenu() {
        document.body.style.overflow = "hidden";
        menuOpened = true;
    }

    function closeNavigationMenu() {
        document.body.style.overflow = "auto";
        menuOpened = false;
    }

    onMount(() => {
        // Check if product id url param is filled
        if (productId) {
            wantedProductPromise = getSpecificProduct(productId);
        }
    });
</script>


<svelte:head>
    <title>{pageData.title} - {pageData.meta.parent.title}</title>
</svelte:head>

<!-- Menu modal -->
{#if menuOpened}
<NavigationMenu bind:menuOpened {closeNavigationMenu} />
{/if}

<Hero src={pageData.hero_image.full_url} heading={pageData.heading} {openNavigationMenu} {data}>
    <div class="h-full w-full flex md:flex-row flex-col gap-4" slot="content">
        <!-- Contact me form -->
        <div class="md:w-1/2 w-full">
            <div class="p-4 pt-0 border-custom rounded-2xl h-full overflow-auto">
                <!-- Heading -->
                <h1 class="heading-underline text-textPrimary text-xl after:h-1.5">Pišite mi</h1>

                <p class="contact-input-heading">Vaši podatki:</p>
                <form action="" method="post" class="flex flex-col gap-4">
                    <!-- Name -->
                    <input bind:value={name} name="name" type="text" class="input" placeholder="Ime" required>

                    <!-- Email -->
                    <input bind:value={email} name="email" type="email" class="input" placeholder="Vaš email" required>

                    <!-- Contact reason -->
                    <div class="w-full text-textPrimary">
                        <p class="contact-input-heading">Zanima me:</p>
                        <div class="flex gap-2">
                            <label class:checked={contactReason == "izdelave po naročilu"} for="customOrder" class="contact-reason">
                                <CustomIcon />
                                <p>Izdelava po naročilu</p>
                            </label>
                            <input name="contact-reason" on:change={(e) => {contactReason = (e.target.checked ? "izdelave po naročilu" : "VAŠ RAZLOG")}} id="customOrder" type="radio" hidden checked>

                            <label class:checked={contactReason == "drugih razlogov"} for="otherReason" class="contact-reason">
                                <PhoneIcon />
                                <p>Drugi razlogi</p>
                            </label>
                            <input name="contact-reason" on:change={(e) => {contactReason = (e.target.checked ? "drugih razlogov" : "VAŠ RAZLOG")}} id="otherReason" type="radio" hidden>
                        </div>
                    </div>

                    <!-- Product type -->
                    {#if contactReason == "izdelave po naročilu" && !wantedProductPromise}
                    <div>
                        <p class="contact-input-heading">Izberite kategorijo:</p>
                        <select name="product-type" class="input-dropdown" id="product-type">
                            {#each productCategories as category}
                            <option value={category.name}>{category.name}</option>
                            {/each}
                            <option value="other">Drugo</option>
                        </select>
                    </div>
                    {/if}
                    
                    <!-- Selected product -->
                    {#if wantedProductPromise}
                    {#await wantedProductPromise}
                    ...nalagam
                    {:then product} 
                    {#if product.error}
                    <Toast type="error">
                        <p>Napaka</p>
                        <ErrorIcon />
                    </Toast>
                    {:else}
                    <!-- Show product preview -->
                    <div>
                        <p class="contact-input-heading mb-2">Izbran izdelek:</p>
                        <div class="w-full h-36 overflow-hidden flex gap-2 relative border-custom p-2 rounded-xl">
                            <!-- Remove btn -->
                            <button on:click={() => {
                                wantedProductPromise = null;
                                
                                // Remove izdelek param
                                const url = new URL(window.location.href);
                                url.searchParams.delete('izdelek');
                                // Update the URL in the browser without reloading the page
                                window.history.pushState({}, '', url);
                            }} class="absolute top-2 right-3 text-white hover:text-red-500 text-lg">
                                <TrashIcon />
                            </button>
                            
                            <img src={product.image[0].image.full_url} alt={product.image[0].image.alt} class="object-contain h-full w-full">
                            <div class="text-textSecondary flex flex-col justify-center">
                                <p class="text-textPrimary">{product.name}</p>
                                <p class="text-sm">{@html product.image_description}</p>
                            </div>
                        </div>
                    </div>
                    {/if}
                    {/await}
                    {/if}

                    <!-- Message -->
                    <div class="w-full">
                        <p class="contact-input-heading">Vaše sporočilo:</p>
                        <textarea name="message" bind:value={message} id="" rows="3" class="input resize-y w-full" placeholder="Ali je možen lovski nož s zelenim epoksi ročajem?" required></textarea>
                    </div>
                    
                    <!-- Submit -->
                    <button type="submit" class="btn mt-4 border-custom">POŠLJI</button>

                    <!-- Success message -->
                    {#if form}
                    <Toast type={(form.success ? 'success' : 'error')}>
                        {#if form.success}
                        <p>Poslano</p>
                        <InfoIcon />
                        {:else}
                        <p>Napaka</p>
                        <ErrorIcon />
                        {/if}
                    </Toast>
                    {/if}
                </form>
            </div>
        </div>
        <!-- Other info: personal info, location/map -->
        <div class="md:w-1/2 w-full flex flex-col gap-4">
            <!-- Personal info -->
            <div class="border-custom rounded-2xl h-1/2 px-8">
                <!-- Heading -->
                <h1 class="heading-underline text-textPrimary text-xl after:h-1.5">Informacije</h1>
                <!-- Content -->
                <ul class="flex flex-col gap-2">
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>email</p>
                        <!-- Info value -->
                        <a href="mailto:{settings.email}">{settings.email}</a>
                    </li>
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>telefon</p>
                        <!-- Info value -->
                        <a href="tel:{settings.phone_number}">{settings.phone_number}</a>
                    </li>
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>naslov</p>
                        <!-- Info value -->
                        <div class="text-end">
                            {@html settings.workshop_address}
                        </div>
                    </li>
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>sledite mi</p>
                        <!-- Info value -->
                        <ul class="flex">
                            <li><a href={settings.instagram_url}><IGIcon /></a></li>
                        </ul>
                    </li>
                </ul>
            </div>
            <!-- Map -->
            <div class="bg-white md:h-1/2 h-full rounded-2xl">
                <!-- svelte-ignore a11y_missing_attribute -->
                <iframe
                    class="w-full h-full min-h-60 rounded-2xl"
                    style="border:0"
                    loading="lazy"
                    allowfullscreen
                    referrerpolicy="no-referrer-when-downgrade"
                    src="https://www.google.com/maps/embed/v1/place?key={PUBLIC_GOOGLE_MAPS_EMBED_API_KEY}
                    &q={settings.workshop_address_raw}">
                </iframe>
            </div>
        </div>
    </div>
</Hero>