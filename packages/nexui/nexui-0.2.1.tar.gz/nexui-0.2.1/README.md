# 🚀 NexUI

NexUI is a UI component library for Django, optimized for HTMX and based on Tailwind CSS. It allows you to easily add interactive elements to your Django applications while benefiting from seamless integration with HTMX for AJAX request handling.

---

## 📌 Installation

### Basic Installation
```bash
pip install nexui
```

### Installation with HTMX support
If you plan to use HTMX with your components:
```bash
pip install nexui[htmx]
```

Or install HTMX separately later:
```bash
pip install django-htmx
```

Add nexui to the list of installed apps in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'nexui',
]
```

---

## 🎨 Features

✅ Reusable UI components for Django  
🔥 Smooth integration with HTMX  
🎨 Based on Tailwind CSS for a modern design  
📦 Easy to install and use  

---

## 🚀 Usage

### Load NexUI tags in your Django templates
```django
{% load nexui_tags %}
```

---

## 📖 Documentation

Check the full documentation here: [Official Documentation](https://github.com/huguescodeur/nexui)

### 🔘 Button Component

The button component allows you to create customizable buttons with icons and HTMX interactions.

#### **Available Options:**
- `label`: Button text
- `type`: Button type (`button`, `submit`, `reset`)
- `button_class`: Custom CSS classes
- `icon`: Icon (supports `Emoji`, `Font Awesome`, and `Unicode`)
- `icon_type`: Icon type (`emoji`, `fa`, `unicode`)
- `icon_position`: Icon position (`left`, `right`)
- `icon_size`: Icon size
- `icon_color`: Icon color
- `disabled`: Disables the button (`true`)
- `url_name`: Django URL name
- `url_params`: Dynamic parameters for the Django URL
- `attrs`: Additional `HTML` and `HTMX` attributes (`_hx-*`, `id`, `style`, `data-*`, etc.)

### **Button Usage Examples:**

#### 1️⃣ Simple Button
```django
{% button label="Send" %}
```

#### 2️⃣ Customized Simple Button
```django
{% button label="Send" type="submit" button_class="bg-yellow-500 text-black" %}
```

#### 3️⃣ Button with HTMX
```django
{% button label="Send with HTMX" type="submit" button_class="bg-green-500" attrs="hx-post='/submit' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 4️⃣ Button with Dynamic URL
```django
{% button label="Dynamic URL Params" type="submit" button_class="bg-blue-500 text-white" url_name="update-user" url_params="2, tomato" attrs="hx-confirm='Are you sure?' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 5️⃣ Button with Emojis
```django
{% button label="Download" button_class="bg-green-500" icon="⬇️" icon_position="left" icon_size="lg" %}
```

### 📝 Input Component

The input component allows you to create customizable input fields with labels, icons, and HTMX integration.

#### **Available Options:**
- `type`: Input type (`text`, `password`, `email`, etc.)
- `name`: Field name
- `id`: Field ID (default is the same as `name`)
- `value`: Default value
- `placeholder`: Placeholder text
- `container_class`: CSS classes for the main container
- `wrapper_class`: CSS classes for the input wrapper
- `label_class`: CSS classes for the label
- `input_class`: CSS classes for the input
- `label`: Label text
- `required`: Required field (`true`/`false`)
- `disabled`: Disables the field (`true`/`false`)
- `readonly`: Read-only field (`true`/`false`)
- `icon`: Icon (supports `Emoji`, `Font Awesome`, and `Unicode`)
- `icon_type`: Icon type (`fa`, `emoji`)
- `icon_position`: Icon position (`left`, `right`)
- `icon_size`: Icon size
- `icon_color`: Icon color
- `url_name`: Django URL name for `HTMX`
- `method`: HTTP method for HTMX (`post` by default)
- `attrs`: Additional `HTML` and `HTMX` attributes

### **Input Usage Examples:**

#### 1️⃣ Simple Input with Label and Icon

##### Simple Input
```django
{% input_field %}
```

##### Simple Input with Label
```django
{% input_field name="email" label="Email" %}
```

##### Simple Input with Label, Icon, and Customization
```django
{% input_field name="email" label="Email" icon="fas fa-envelope" icon_type="fa" icon_position="left" placeholder="Email" %}
```

#### 2️⃣ Password Input with Emoji
```django
{% input_field type="password" icon="🔒" %}
```

#### 3️⃣ Input with HTMX and Confirmation
```django
{% input_field name="email" label="Email" icon="fas fa-envelope" icon_type="fa" url_name="submit-form" attrs='hx-confirm="Are you okay?"' %}
```

#### 4️⃣ Input with Real-Time Search
```django
{% input_field name="search" label="Search" icon="fas fa-search" icon_type="fa" icon_position="left" url_name="search_suggestions" attrs='hx-trigger="keyup changed delay:500ms" hx-target="#suggestions"' %}
```

#### 5️⃣ Custom Styled Input
```django
{% input_field container_class="py-2 flex items-center" name="email" label="Email" label_class="ml-2 text-gray-700 font-bold" input_class="w-44 pl-10 pr-3 py-2 rounded-md border border-gray-300" icon="fas fa-envelope" icon_type="fa" icon_position="left" %}
```

---

## 💡 Contribute

The project is currently in its early testing phase. We encourage interested users to provide feedback on the library.

If you want to contribute to **NexUI** or have suggestions:

1. **`Fork` the project** 📌
2. **`Test` the components and provide feedback** 🛠️
3. **`Create` an issue** to share your suggestions or report problems ✅

We cannot accept direct contributions at the moment, but **your feedback is essential** for NexUI's evolution.

---

## 🔗 Useful Links

- [GitHub Repository](https://github.com/huguescodeur/nexui) 🖥️
- [Report a Bug](https://github.com/huguescodeur/nexui/issues) 🐞
- [Django-HTMX](https://django-htmx.readthedocs.io/en/latest/installation.html) ⚡
- [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) 🎨
- [HTMX](https://htmx.org/) ⚡
- [Tailwind CSS](https://tailwindcss.com/) 🎨

---

## ⚖️ License

This project is licensed under the **MIT** license. See the LICENSE file for more details.

![PyPI - Downloads](https://img.shields.io/pypi/dm/nexui)

