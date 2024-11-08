<script>
    // Components
    import Hero from "$lib/components/Hero.svelte";
    // Icons
    import PhoneIcon from '~icons/mdi/phone';
    import CustomIcon from '~icons/gridicons/customize';
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    // Secrets
    import {
        PUBLIC_GOOGLE_MAPS_EMBED_API_KEY
    } from "$env/static/public";

    export let data;
    $: page = data.contact;
    $: settings = data.settings

    let name;
    let email;
    let contactReason = "izdelave po naročilu";
    let message;
    let productType;
</script>


<svelte:head>
    <title>{page.title}</title>
</svelte:head>


<Hero src={page.hero_image.full_url} heading={page.heading} {data}>
    <div class="h-full w-full flex md:flex-row flex-col gap-4" slot="content">
        <!-- Contact me form -->
        <div class="md:w-1/2 w-full">
            <div class="p-4 pt-0 border-custom rounded-2xl h-full overflow-auto">
                <!-- Heading -->
                <h1 class="heading-underline text-textPrimary text-xl after:h-1.5">Pišite mi</h1>

                <p class="contact-input-heading">Vasi podatki:</p>
                <form action="" method="post" class="flex flex-col gap-4">
                    <!-- Name -->
                    <input bind:value={name} type="text" class="input" placeholder="Ime" required>
                    <!-- Email -->
                    <input bind:value={email} type="email" class="input" placeholder="Vaš email" required>
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
                    <!-- Message -->
                    {#if contactReason == "drugih razlogov"}
                    <textarea bind:value={message} name="" id="" rows="5" class="input resize-y" placeholder="Sporočilo" required></textarea>
                    <!-- Product type -->
                    {:else if contactReason == "izdelave po naročilu"}
                    <div>
                        <p class="contact-input-heading">Izberite kategorijo:</p>
                        <select bind:value={productType} name="product-type" class="input-dropdown" id="product-type">
                            <optgroup label="Nozi:">
                                <option value="kitchen-knife">Kuhinjski noz</option>
                                <option value="hunting-knife">Lovski noz</option>
                            </optgroup>
                            <optgroup label="Obeski:">
                                <option value="">Obesek srce</option>
                                <option value="">Obesek metulj</option>
                            </optgroup>
                            <option value="other">Drugo</option>
                        </select>
                    </div>
                    {/if}

                    <!-- Message preview -->
                    {#if name}
                    <div class="text-textSecondary my-4 w-full">
                        <p class="contact-input-heading">Preogled sporočila (sporočilo lahko urejate):</p>
                        <p contenteditable class="w-full text-wrap">
                            Zdravo, sem <span class="text-white font-bold">{name}</span>.<br>
                            Pisem vam glede <span class="text-white font-bold">{contactReason}</span>.<br>
                            <br>
                            {#if contactReason == "drugih razlogov"}
                            {message}
                            {:else if contactReason == "izdelave po naročilu"}
                            Zanima me izdelek: {productType}
                            {/if}
                        </p>
                    </div>
                    {/if}
                    <!-- Submit -->
                    <button type="submit" class="btn mt-4">POŠLJI</button>
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
                    class="w-full h-full rounded-2xl"
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