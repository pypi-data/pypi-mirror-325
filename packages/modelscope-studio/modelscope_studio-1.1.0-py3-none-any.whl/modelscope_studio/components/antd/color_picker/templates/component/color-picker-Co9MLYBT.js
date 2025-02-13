import { i as pe, a as H, r as me, g as _e, w as O, d as he, b as k, c as ge } from "./Index-B17pgqlL.js";
const C = window.ms_globals.React, L = window.ms_globals.React.useMemo, ne = window.ms_globals.React.useState, re = window.ms_globals.React.useEffect, de = window.ms_globals.React.forwardRef, fe = window.ms_globals.React.useRef, W = window.ms_globals.ReactDOM.createPortal, xe = window.ms_globals.internalContext.useContextPropsContext, j = window.ms_globals.internalContext.ContextPropsProvider, be = window.ms_globals.antd.ColorPicker, we = window.ms_globals.createItemsContext.createItemsContext;
var ye = /\s/;
function Ee(e) {
  for (var t = e.length; t-- && ye.test(e.charAt(t)); )
    ;
  return t;
}
var Ie = /^\s+/;
function Ce(e) {
  return e && e.slice(0, Ee(e) + 1).replace(Ie, "");
}
var G = NaN, ve = /^[-+]0x[0-9a-f]+$/i, Se = /^0b[01]+$/i, Re = /^0o[0-7]+$/i, ke = parseInt;
function z(e) {
  if (typeof e == "number")
    return e;
  if (pe(e))
    return G;
  if (H(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = H(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ce(e);
  var o = Se.test(e);
  return o || Re.test(e) ? ke(e.slice(2), o ? 2 : 8) : ve.test(e) ? G : +e;
}
var F = function() {
  return me.Date.now();
}, Oe = "Expected a function", Te = Math.max, Pe = Math.min;
function je(e, t, o) {
  var l, s, n, r, i, a, _ = 0, g = !1, c = !1, x = !0;
  if (typeof e != "function")
    throw new TypeError(Oe);
  t = z(t) || 0, H(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Te(z(o.maxWait) || 0, t) : n, x = "trailing" in o ? !!o.trailing : x);
  function d(h) {
    var I = l, R = s;
    return l = s = void 0, _ = h, r = e.apply(R, I), r;
  }
  function b(h) {
    return _ = h, i = setTimeout(m, t), g ? d(h) : r;
  }
  function u(h) {
    var I = h - a, R = h - _, U = t - I;
    return c ? Pe(U, n - R) : U;
  }
  function p(h) {
    var I = h - a, R = h - _;
    return a === void 0 || I >= t || I < 0 || c && R >= n;
  }
  function m() {
    var h = F();
    if (p(h))
      return w(h);
    i = setTimeout(m, u(h));
  }
  function w(h) {
    return i = void 0, x && l ? d(h) : (l = s = void 0, r);
  }
  function y() {
    i !== void 0 && clearTimeout(i), _ = 0, l = a = s = i = void 0;
  }
  function f() {
    return i === void 0 ? r : w(F());
  }
  function v() {
    var h = F(), I = p(h);
    if (l = arguments, s = this, a = h, I) {
      if (i === void 0)
        return b(a);
      if (c)
        return clearTimeout(i), i = setTimeout(m, t), d(a);
    }
    return i === void 0 && (i = setTimeout(m, t)), r;
  }
  return v.cancel = y, v.flush = f, v;
}
var oe = {
  exports: {}
}, A = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Le = C, Ae = Symbol.for("react.element"), Fe = Symbol.for("react.fragment"), Ne = Object.prototype.hasOwnProperty, We = Le.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, He = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function se(e, t, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Ne.call(t, l) && !He.hasOwnProperty(l) && (s[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) s[l] === void 0 && (s[l] = t[l]);
  return {
    $$typeof: Ae,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: We.current
  };
}
A.Fragment = Fe;
A.jsx = se;
A.jsxs = se;
oe.exports = A;
var E = oe.exports;
const {
  SvelteComponent: Me,
  assign: q,
  binding_callbacks: V,
  check_outros: De,
  children: le,
  claim_element: ie,
  claim_space: Be,
  component_subscribe: J,
  compute_slots: Ue,
  create_slot: Ge,
  detach: S,
  element: ce,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: ze,
  get_slot_changes: qe,
  group_outros: Ve,
  init: Je,
  insert_hydration: T,
  safe_not_equal: Xe,
  set_custom_element_data: ae,
  space: Ye,
  transition_in: P,
  transition_out: M,
  update_slot_base: Ke
} = window.__gradio__svelte__internal, {
  beforeUpdate: Qe,
  getContext: Ze,
  onDestroy: $e,
  setContext: et
} = window.__gradio__svelte__internal;
function K(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = Ge(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ce("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ie(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = le(t);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      ae(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ke(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? qe(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : ze(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(s, n), o = !0);
    },
    o(n) {
      M(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function tt(e) {
  let t, o, l, s, n = (
    /*$$slots*/
    e[4].default && K(e)
  );
  return {
    c() {
      t = ce("react-portal-target"), o = Ye(), n && n.c(), l = X(), this.h();
    },
    l(r) {
      t = ie(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), le(t).forEach(S), o = Be(r), n && n.l(r), l = X(), this.h();
    },
    h() {
      ae(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      T(r, t, i), e[8](t), T(r, o, i), n && n.m(r, i), T(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && P(n, 1)) : (n = K(r), n.c(), P(n, 1), n.m(l.parentNode, l)) : n && (Ve(), M(n, 1, 1, () => {
        n = null;
      }), De());
    },
    i(r) {
      s || (P(n), s = !0);
    },
    o(r) {
      M(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(l)), e[8](null), n && n.d(r);
    }
  };
}
function Q(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function nt(e, t, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Ue(n);
  let {
    svelteInit: a
  } = t;
  const _ = O(Q(t)), g = O();
  J(e, g, (f) => o(0, l = f));
  const c = O();
  J(e, c, (f) => o(1, s = f));
  const x = [], d = Ze("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: u,
    subSlotIndex: p
  } = _e() || {}, m = a({
    parent: d,
    props: _,
    target: g,
    slot: c,
    slotKey: b,
    slotIndex: u,
    subSlotIndex: p,
    onDestroy(f) {
      x.push(f);
    }
  });
  et("$$ms-gr-react-wrapper", m), Qe(() => {
    _.set(Q(t));
  }), $e(() => {
    x.forEach((f) => f());
  });
  function w(f) {
    V[f ? "unshift" : "push"](() => {
      l = f, g.set(l);
    });
  }
  function y(f) {
    V[f ? "unshift" : "push"](() => {
      s = f, c.set(s);
    });
  }
  return e.$$set = (f) => {
    o(17, t = q(q({}, t), Y(f))), "svelteInit" in f && o(5, a = f.svelteInit), "$$scope" in f && o(6, r = f.$$scope);
  }, t = Y(t), [l, s, g, c, i, a, r, n, w, y];
}
class rt extends Me {
  constructor(t) {
    super(), Je(this, t, nt, tt, Xe, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, N = window.ms_globals.tree;
function ot(e, t = {}) {
  function o(l) {
    const s = O(), n = new rt({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], Z({
            createPortal: W,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((_) => _.svelteInstance !== s), Z({
              createPortal: W,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
function st(e) {
  const [t, o] = ne(() => k(e));
  return re(() => {
    let l = !0;
    return e.subscribe((n) => {
      l && (l = !1, n === t) || o(n);
    });
  }, [e]), t;
}
function lt(e) {
  const t = L(() => he(e, (o) => o), [e]);
  return st(t);
}
function it(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ct(e, t = !1) {
  try {
    if (ge(e))
      return e;
    if (t && !it(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function $(e, t) {
  return L(() => ct(e, t), [e, t]);
}
function at(e, t) {
  const o = L(() => C.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && (!n.props.nodeSlotKey || t)).sort((n, r) => {
    if (n.props.node.slotIndex && r.props.node.slotIndex) {
      const i = k(n.props.node.slotIndex) || 0, a = k(r.props.node.slotIndex) || 0;
      return i - a === 0 && n.props.node.subSlotIndex && r.props.node.subSlotIndex ? (k(n.props.node.subSlotIndex) || 0) - (k(r.props.node.subSlotIndex) || 0) : i - a;
    }
    return 0;
  }).map((n) => n.props.node.target), [e, t]);
  return lt(o);
}
const ut = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function dt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return t[o] = ft(o, l), t;
  }, {}) : {};
}
function ft(e, t) {
  return typeof t == "number" && !ut.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...C.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      o.addEventListener(i, r, a);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(n);
      t.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function pt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const B = de(({
  slot: e,
  clone: t,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = fe(), [i, a] = ne([]), {
    forceClone: _
  } = xe(), g = _ ? !0 : t;
  return re(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function x() {
      let u = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (u = c.children[0], u.tagName.toLowerCase() === "react-portal-target" && u.children[0] && (u = u.children[0])), pt(n, u), o && u.classList.add(...o.split(" ")), l) {
        const p = dt(l);
        Object.keys(p).forEach((m) => {
          u.style[m] = p[m];
        });
      }
    }
    let d = null;
    if (g && window.MutationObserver) {
      let u = function() {
        var y, f, v;
        (y = r.current) != null && y.contains(c) && ((f = r.current) == null || f.removeChild(c));
        const {
          portals: m,
          clonedElement: w
        } = D(e);
        c = w, a(m), c.style.display = "contents", x(), (v = r.current) == null || v.appendChild(c);
      };
      u();
      const p = je(() => {
        u(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      d = new window.MutationObserver(p), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", x(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var u, p;
      c.style.display = "", (u = r.current) != null && u.contains(c) && ((p = r.current) == null || p.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, g, o, l, n, s]), C.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function ue(e, t, o) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((s, n) => {
      var _;
      if (typeof s != "object")
        return s;
      const r = {
        ...s.props,
        key: ((_ = s.props) == null ? void 0 : _.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(s.slots).forEach((g) => {
        if (!s.slots[g] || !(s.slots[g] instanceof Element) && !s.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((m, w) => {
          i[m] || (i[m] = {}), w !== c.length - 1 && (i = r[m]);
        });
        const x = s.slots[g];
        let d, b, u = !1, p = t == null ? void 0 : t.forceClone;
        x instanceof Element ? d = x : (d = x.el, b = x.callback, u = x.clone ?? u, p = x.forceClone ?? p), p = p ?? !!b, i[c[c.length - 1]] = d ? b ? (...m) => (b(c[c.length - 1], m), /* @__PURE__ */ E.jsx(j, {
          params: m,
          forceClone: p,
          children: /* @__PURE__ */ E.jsx(B, {
            slot: d,
            clone: u
          })
        })) : /* @__PURE__ */ E.jsx(j, {
          forceClone: p,
          children: /* @__PURE__ */ E.jsx(B, {
            slot: d,
            clone: u
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = "children";
      return s[a] && (r[a] = ue(s[a], t, `${n}`)), r;
    });
}
function ee(e, t) {
  return e ? /* @__PURE__ */ E.jsx(B, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function te({
  key: e,
  slots: t,
  targets: o
}, l) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ E.jsx(j, {
    params: s,
    forceClone: !0,
    children: ee(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ E.jsx(j, {
    params: s,
    forceClone: !0,
    children: ee(t[e], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  withItemsContextProvider: mt,
  useItems: _t,
  ItemHandler: gt
} = we("antd-color-picker-presets"), xt = ot(mt(["presets"], ({
  onValueChange: e,
  onChange: t,
  panelRender: o,
  showText: l,
  value: s,
  presets: n,
  children: r,
  value_format: i,
  setSlotParams: a,
  slots: _,
  ...g
}) => {
  const c = $(o), x = $(l), d = at(r), {
    items: {
      presets: b
    }
  } = _t();
  return /* @__PURE__ */ E.jsxs(E.Fragment, {
    children: [d.length === 0 && /* @__PURE__ */ E.jsx("div", {
      style: {
        display: "none"
      },
      children: r
    }), /* @__PURE__ */ E.jsx(be, {
      ...g,
      value: s,
      presets: L(() => n || ue(b), [n, b]),
      showText: _.showText ? te({
        slots: _,
        setSlotParams: a,
        key: "showText"
      }) : x || l,
      panelRender: _.panelRender ? te({
        slots: _,
        setSlotParams: a,
        key: "panelRender"
      }) : c,
      onChange: (u, ...p) => {
        if (u.isGradient()) {
          const w = u.getColors().map((y) => {
            const f = {
              rgb: y.color.toRgbString(),
              hex: y.color.toHexString(),
              hsb: y.color.toHsbString()
            };
            return {
              ...y,
              color: f[i]
            };
          });
          t == null || t(w, ...p), e(w);
          return;
        }
        const m = {
          rgb: u.toRgbString(),
          hex: u.toHexString(),
          hsb: u.toHsbString()
        };
        t == null || t(m[i], ...p), e(m[i]);
      },
      children: d.length === 0 ? null : r
    })]
  });
}));
export {
  xt as ColorPicker,
  xt as default
};
