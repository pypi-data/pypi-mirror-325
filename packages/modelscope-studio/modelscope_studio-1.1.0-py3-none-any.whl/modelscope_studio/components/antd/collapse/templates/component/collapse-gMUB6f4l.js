import { i as ue, a as W, r as de, g as fe, w as k, b as me } from "./Index-VvIBYTLs.js";
const v = window.ms_globals.React, Z = window.ms_globals.React.useMemo, oe = window.ms_globals.React.forwardRef, ie = window.ms_globals.React.useRef, ce = window.ms_globals.React.useState, ae = window.ms_globals.React.useEffect, F = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, T = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Collapse, pe = window.ms_globals.createItemsContext.createItemsContext;
var ge = /\s/;
function be(t) {
  for (var e = t.length; e-- && ge.test(t.charAt(e)); )
    ;
  return e;
}
var we = /^\s+/;
function xe(t) {
  return t && t.slice(0, be(t) + 1).replace(we, "");
}
var B = NaN, ye = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Ce = parseInt;
function H(t) {
  if (typeof t == "number")
    return t;
  if (ue(t))
    return B;
  if (W(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = W(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = xe(t);
  var l = Ee.test(t);
  return l || ve.test(t) ? Ce(t.slice(2), l ? 2 : 8) : ye.test(t) ? B : +t;
}
var L = function() {
  return de.Date.now();
}, Ie = "Expected a function", Se = Math.max, Re = Math.min;
function ke(t, e, l) {
  var o, s, n, r, i, a, g = 0, h = !1, c = !1, b = !0;
  if (typeof t != "function")
    throw new TypeError(Ie);
  e = H(e) || 0, W(l) && (h = !!l.leading, c = "maxWait" in l, n = c ? Se(H(l.maxWait) || 0, e) : n, b = "trailing" in l ? !!l.trailing : b);
  function d(_) {
    var E = o, R = s;
    return o = s = void 0, g = _, r = t.apply(R, E), r;
  }
  function w(_) {
    return g = _, i = setTimeout(p, e), h ? d(_) : r;
  }
  function f(_) {
    var E = _ - a, R = _ - g, U = e - E;
    return c ? Re(U, n - R) : U;
  }
  function m(_) {
    var E = _ - a, R = _ - g;
    return a === void 0 || E >= e || E < 0 || c && R >= n;
  }
  function p() {
    var _ = L();
    if (m(_))
      return y(_);
    i = setTimeout(p, f(_));
  }
  function y(_) {
    return i = void 0, b && o ? d(_) : (o = s = void 0, r);
  }
  function C() {
    i !== void 0 && clearTimeout(i), g = 0, o = a = s = i = void 0;
  }
  function u() {
    return i === void 0 ? r : y(L());
  }
  function I() {
    var _ = L(), E = m(_);
    if (o = arguments, s = this, a = _, E) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(p, e), d(a);
    }
    return i === void 0 && (i = setTimeout(p, e)), r;
  }
  return I.cancel = C, I.flush = u, I;
}
var $ = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = v, Pe = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ne = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ee(t, e, l) {
  var o, s = {}, n = null, r = null;
  l !== void 0 && (n = "" + l), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (o in e) je.call(e, o) && !Ne.hasOwnProperty(o) && (s[o] = e[o]);
  if (t && t.defaultProps) for (o in e = t.defaultProps, e) s[o] === void 0 && (s[o] = e[o]);
  return {
    $$typeof: Pe,
    type: t,
    key: n,
    ref: r,
    props: s,
    _owner: Le.current
  };
}
j.Fragment = Te;
j.jsx = ee;
j.jsxs = ee;
$.exports = j;
var x = $.exports;
const {
  SvelteComponent: Fe,
  assign: z,
  binding_callbacks: G,
  check_outros: We,
  children: te,
  claim_element: ne,
  claim_space: Ae,
  component_subscribe: q,
  compute_slots: Me,
  create_slot: De,
  detach: S,
  element: re,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Ue,
  get_slot_changes: Be,
  group_outros: He,
  init: ze,
  insert_hydration: O,
  safe_not_equal: Ge,
  set_custom_element_data: se,
  space: qe,
  transition_in: P,
  transition_out: A,
  update_slot_base: Ve
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Ke
} = window.__gradio__svelte__internal;
function X(t) {
  let e, l;
  const o = (
    /*#slots*/
    t[7].default
  ), s = De(
    o,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = re("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      e = ne(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = te(e);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, e, r), s && s.m(e, null), t[9](e), l = !0;
    },
    p(n, r) {
      s && s.p && (!l || r & /*$$scope*/
      64) && Ve(
        s,
        o,
        n,
        /*$$scope*/
        n[6],
        l ? Be(
          o,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ue(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      l || (P(s, n), l = !0);
    },
    o(n) {
      A(s, n), l = !1;
    },
    d(n) {
      n && S(e), s && s.d(n), t[9](null);
    }
  };
}
function Qe(t) {
  let e, l, o, s, n = (
    /*$$slots*/
    t[4].default && X(t)
  );
  return {
    c() {
      e = re("react-portal-target"), l = qe(), n && n.c(), o = V(), this.h();
    },
    l(r) {
      e = ne(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), te(e).forEach(S), l = Ae(r), n && n.l(r), o = V(), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, e, i), t[8](e), O(r, l, i), n && n.m(r, i), O(r, o, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && P(n, 1)) : (n = X(r), n.c(), P(n, 1), n.m(o.parentNode, o)) : n && (He(), A(n, 1, 1, () => {
        n = null;
      }), We());
    },
    i(r) {
      s || (P(n), s = !0);
    },
    o(r) {
      A(n), s = !1;
    },
    d(r) {
      r && (S(e), S(l), S(o)), t[8](null), n && n.d(r);
    }
  };
}
function Y(t) {
  const {
    svelteInit: e,
    ...l
  } = t;
  return l;
}
function Ze(t, e, l) {
  let o, s, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = Me(n);
  let {
    svelteInit: a
  } = e;
  const g = k(Y(e)), h = k();
  q(t, h, (u) => l(0, o = u));
  const c = k();
  q(t, c, (u) => l(1, s = u));
  const b = [], d = Xe("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m
  } = fe() || {}, p = a({
    parent: d,
    props: g,
    target: h,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(u) {
      b.push(u);
    }
  });
  Ke("$$ms-gr-react-wrapper", p), Je(() => {
    g.set(Y(e));
  }), Ye(() => {
    b.forEach((u) => u());
  });
  function y(u) {
    G[u ? "unshift" : "push"](() => {
      o = u, h.set(o);
    });
  }
  function C(u) {
    G[u ? "unshift" : "push"](() => {
      s = u, c.set(s);
    });
  }
  return t.$$set = (u) => {
    l(17, e = z(z({}, e), J(u))), "svelteInit" in u && l(5, a = u.svelteInit), "$$scope" in u && l(6, r = u.$$scope);
  }, e = J(e), [o, s, h, c, i, a, r, n, y, C];
}
class $e extends Fe {
  constructor(e) {
    super(), ze(this, e, Ze, Qe, Ge, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, N = window.ms_globals.tree;
function et(t, e = {}) {
  function l(o) {
    const s = k(), n = new $e({
      ...o,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], K({
            createPortal: F,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((g) => g.svelteInstance !== s), K({
              createPortal: F,
              node: N
            });
          }), i;
        },
        ...o.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(l);
    });
  });
}
function tt(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function nt(t, e = !1) {
  try {
    if (me(t))
      return t;
    if (e && !tt(t))
      return;
    if (typeof t == "string") {
      let l = t.trim();
      return l.startsWith(";") && (l = l.slice(1)), l.endsWith(";") && (l = l.slice(0, -1)), new Function(`return (...args) => (${l})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function rt(t, e) {
  return Z(() => nt(t, e), [t, e]);
}
const st = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function lt(t) {
  return t ? Object.keys(t).reduce((e, l) => {
    const o = t[l];
    return e[l] = ot(l, o), e;
  }, {}) : {};
}
function ot(t, e) {
  return typeof e == "number" && !st.includes(t) ? e + "px" : e;
}
function M(t) {
  const e = [], l = t.cloneNode(!1);
  if (t._reactElement) {
    const s = v.Children.toArray(t._reactElement.props.children).map((n) => {
      if (v.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = M(n.props.el);
        return v.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...v.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = t._reactElement.props.children, e.push(F(v.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: s
    }), l)), {
      clonedElement: l,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((s) => {
    t.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      l.addEventListener(i, r, a);
    });
  });
  const o = Array.from(t.childNodes);
  for (let s = 0; s < o.length; s++) {
    const n = o[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = M(n);
      e.push(...i), l.appendChild(r);
    } else n.nodeType === 3 && l.appendChild(n.cloneNode());
  }
  return {
    clonedElement: l,
    portals: e
  };
}
function it(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const D = oe(({
  slot: t,
  clone: e,
  className: l,
  style: o,
  observeAttributes: s
}, n) => {
  const r = ie(), [i, a] = ce([]), {
    forceClone: g
  } = _e(), h = g ? !0 : e;
  return ae(() => {
    var w;
    if (!r.current || !t)
      return;
    let c = t;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), it(n, f), l && f.classList.add(...l.split(" ")), o) {
        const m = lt(o);
        Object.keys(m).forEach((p) => {
          f.style[p] = m[p];
        });
      }
    }
    let d = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var C, u, I;
        (C = r.current) != null && C.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: p,
          clonedElement: y
        } = M(t);
        c = y, a(p), c.style.display = "contents", b(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const m = ke(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      d = new window.MutationObserver(m), d.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [t, h, l, o, n, s]), v.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function le(t, e, l) {
  const o = t.filter(Boolean);
  if (o.length !== 0)
    return o.map((s, n) => {
      var g;
      if (typeof s != "object")
        return e != null && e.fallback ? e.fallback(s) : s;
      const r = {
        ...s.props,
        key: ((g = s.props) == null ? void 0 : g.key) ?? (l ? `${l}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(s.slots).forEach((h) => {
        if (!s.slots[h] || !(s.slots[h] instanceof Element) && !s.slots[h].el)
          return;
        const c = h.split(".");
        c.forEach((p, y) => {
          i[p] || (i[p] = {}), y !== c.length - 1 && (i = r[p]);
        });
        const b = s.slots[h];
        let d, w, f = (e == null ? void 0 : e.clone) ?? !1, m = e == null ? void 0 : e.forceClone;
        b instanceof Element ? d = b : (d = b.el, w = b.callback, f = b.clone ?? f, m = b.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = d ? w ? (...p) => (w(c[c.length - 1], p), /* @__PURE__ */ x.jsx(T, {
          params: p,
          forceClone: m,
          children: /* @__PURE__ */ x.jsx(D, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ x.jsx(T, {
          forceClone: m,
          children: /* @__PURE__ */ x.jsx(D, {
            slot: d,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return s[a] ? r[a] = le(s[a], e, `${n}`) : e != null && e.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
function Q(t, e) {
  return t ? /* @__PURE__ */ x.jsx(D, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function ct({
  key: t,
  slots: e,
  targets: l
}, o) {
  return e[t] ? (...s) => l ? l.map((n, r) => /* @__PURE__ */ x.jsx(T, {
    params: s,
    forceClone: !0,
    children: Q(n, {
      clone: !0,
      ...o
    })
  }, r)) : /* @__PURE__ */ x.jsx(T, {
    params: s,
    forceClone: !0,
    children: Q(e[t], {
      clone: !0,
      ...o
    })
  }) : void 0;
}
const {
  withItemsContextProvider: at,
  useItems: ut,
  ItemHandler: ft
} = pe("antd-collapse-items"), mt = et(at(["default", "items"], ({
  slots: t,
  items: e,
  children: l,
  onChange: o,
  setSlotParams: s,
  expandIcon: n,
  ...r
}) => {
  const {
    items: i
  } = ut(), a = i.items.length > 0 ? i.items : i.default, g = rt(n);
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: l
    }), /* @__PURE__ */ x.jsx(he, {
      ...r,
      onChange: (h) => {
        o == null || o(h);
      },
      expandIcon: t.expandIcon ? ct({
        slots: t,
        setSlotParams: s,
        key: "expandIcon"
      }) : g,
      items: Z(() => e || le(a, {
        // for the children slot
        // clone: true,
      }), [e, a])
    })]
  });
}));
export {
  mt as Collapse,
  mt as default
};
